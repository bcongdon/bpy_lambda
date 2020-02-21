# Docker file for building Blender as a Python module for AWS Lambda
# Compiles to ~/blender-git/blender_build/bin
FROM amazonlinux:2018.03
RUN yum install git cmake -y
RUN yum groupinstall 'Development Tools' -y

RUN yum install gcc-c++ \
    libXi-devel openexr-devel SDL-devel fftw-devel libtiff-devel \
    freetype-devel libogg-devel libjpeg-devel openjpeg openjpeg-devel \
    libpng-devel vim libGLU-devel wget -y

# Install Python3.6
ENV LD_LIBRARY_PATH /usr/local/lib
RUN cd ~ && \
    wget https://www.python.org/ftp/python/3.6.6/Python-3.6.6.tgz && \
    tar xzf Python-3.6.6.tgz && \
    cd Python-3.6.6 && \
    ./configure --enable-shared && \
    make install && \
    ldconfig && python3 --version

RUN git clone https://github.com/nigels-com/glew ~/glew && \
    cd ~/glew && \
    make extensions && \
    make && \
    make install

RUN mkdir ~/blender-git && \
    cd ~/blender-git && \
    git clone --progress --no-checkout https://git.blender.org/blender.git && \
    cd blender && \
    git checkout tags/v2.79 && \
    git submodule update --init --recursive && \
    git submodule foreach git checkout master && \
    git submodule foreach git pull --rebase origin master

RUN ~/blender-git/blender/build_files/build_environment/install_deps.sh \
    --no-sudo \
    --no-confirm \
    --build-boost \
    --build-openexr \
    --build-oiio \
    --skip-python \
    --skip-numpy \
    --skip-ocio \
    --skip-osl \
    --skip-osd \
    --skip-openvdb \
    --skip-llvm \
    --skip-alembic \
    --skip-opencollada \
    --skip-ffmpeg

ENV BOOST_ROOT ~/src/blender-deps/boost-1.60.0

# Maintainer's note: calculate DPYTHON_INCLUDE_DIR with the following command:
# ```
# python3 -c "from distutils.sysconfig import get_python_inc; print(get_python_inc())"
# ```
RUN mkdir ~/blender-git/blender_build && \
    cd ~/blender-git/blender_build && \
    cmake ../blender \
    -DPYTHON_INCLUDE_DIR=/usr/local/include/python3.6m  \
    -DPYTHON_LIBRARY=/usr/local/lib/libpython3.6m.so \
    -DPYTHON_LIBPATH=/usr/local/lib \
    -DWITH_INTERNATIONAL=OFF \
    -DWITH_CYCLES=ON \
    -DWITH_AUDASPACE=OFF \
    -DWITH_BOOST=ON \
    -DWITH_BULLET=OFF \
    -DWITH_CODEC_AVI=OFF \
    -DWITH_COMPOSITOR=OFF \
    -DWITH_GAMEENGINE=OFF \
    -DWITH_GAMEENGINE_DECKLINK=OFF \
    -DWITH_HEADLESS=ON \
    -DWITH_IMAGE_DDS=OFF \
    -DWITH_IMAGE_CINEON=OFF \
    -DWITH_IMAGE_OPENEXR=OFF \
    -DWITH_IMAGE_OPENJPEG=OFF \
    -DWITH_IMAGE_TIFF=OFF \
    -DWITH_INPUT_NDOF=OFF \
    -DWITH_LIBMV=OFF \
    -DWITH_MOD_REMESH=ON \
    -DWITH_MOD_SMOKE=OFF \
    -DWITH_OPENAL=OFF \
    -DWITH_OPENIMAGEIO=OFF \
    -DWITH_PYTHON_INSTALL_NUMPY=OFF \
    -DWITH_INSTALL_PORTABLE=ON \
    -DWITH_PYTHON_INSTALL_REQUESTS=OFF \
    -DWITH_PYTHON_MODULE=ON \
    -DWITH_PYTHON_INSTALL=OFF \
    -DWITH_STATIC_LIBS=ON \
    -DWITH_SYSTEM_GLEW=OFF \
    -DWITH_SYSTEM_GLES=OFF \
    -DWITH_FREESTYLE=ON

RUN cd ~/blender-git/blender_build && \
    make && \
    make install

RUN mkdir /bpy_lambda && \
    cd /bpy_lambda && \
    cp -R ~/blender-git/blender_build/bin/2.79 . && \
    cp -R ~/blender-git/blender_build/bin/bpy.so . && \
    cp -L /opt/lib/openexr-2.2.0/lib/libHalf.so.12 . && \
    cp -L /opt/lib/openexr-2.2.0/lib/libIex.so.12 . && \
    cp -L /opt/lib/openexr-2.2.0/lib/libIlmImf.so.22 . && \
    cp -L /opt/lib/openexr-2.2.0/lib/libIlmThread.so.12 . && \
    cp -L /opt/lib/openexr-2.2.0/lib/libImath.so.12 . && \
    cp -L /opt/lib/oiio-1.7.15/lib/libOpenImageIO.so.1.7 . && \
    cp -L /usr/lib64/libopenjpeg.so.2 . && \
    cp -L /opt/lib/boost-1.60.0/lib/libboost_filesystem.so.1.60.0 . && \
    cp -L /opt/lib/boost-1.60.0/lib/libboost_regex.so.1.60.0 . && \
    cp -L /opt/lib/boost/lib/libboost_system.so.1.60.0 . && \
    cp -L /opt/lib/boost/lib/libboost_thread.so.1.60.0 . && \
    cp -L /usr/local/lib/libpython3.6m.so.1.0 . && \
    cp -L /usr/lib64/libGLU.so.1 .

# Build artifact stored in /bpy_lambda
