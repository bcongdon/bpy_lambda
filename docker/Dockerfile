# Docker file for building Blender as a Python module for AWS Lambda
# Compiles to ~/blender-git/blender_build/bin
FROM amazonlinux:2018.03
RUN yum groupinstall 'Development Tools' -y
RUN yum install gcc72 gcc72-c++ git subversion make libX11-devel libXi-devel libXcursor-devel libXrandr-devel libXinerama-devel libstdc++-static \
    libtiff-devel libpng-devel libjpeg-devel openjpeg openjpeg-devel freetype-devel \
    wget -y

RUN wget https://cmake.org/files/v3.10/cmake-3.10.0.tar.gz && \
    tar -xvzf cmake-3.10.0.tar.gz && \
    cd cmake-3.10.0 && \
    ./bootstrap && \
    make && \
    make install

# Install Python3.7
#ENV LD_LIBRARY_PATH /usr/local/lib
#RUN cd ~ && \
#    wget https://www.python.org/ftp/python/3.7.8/Python-3.7.8.tgz && \
#    tar xzf Python-3.7.8.tgz && \
#    cd Python-3.7.8 && \
#    ./configure --enable-shared && \
#    make install && \
#    ldconfig && python3 --version

RUN yum install libXmu-devel libXi-devel libGL-devel -y
RUN git clone https://github.com/nigels-com/glew ~/glew && \
    cd ~/glew && \
    make extensions && \
    make && \
    make install

RUN mkdir ~/blender-git && \
    cd ~/blender-git && \
    git clone --progress --no-checkout https://git.blender.org/blender.git && \
    cd blender && \
    git checkout tags/v2.83.1 && \
    git submodule update --init --recursive && \
    git submodule foreach git checkout master && \
    git submodule foreach git pull --rebase origin master

RUN yum install bzip2 sudo libffi libffi-devel freeglut-devel fftw-devel -y
RUN cd ~/blender-git && \
    ./blender/build_files/build_environment/install_deps.sh \
    --no-sudo \
    --no-confirm \
    --skip-numpy \
    --skip-openvdb \
    --skip-ffmpeg \
    --skip-usd

RUN cd ~/blender-git/blender && \
    make -j8 BUILD_CMAKE_ARGS="-U *SNDFILE* -U PYTHON* -U *BOOST* -U *Boost* -U *OPENCOLORIO* -U *OPENEXR* -U *OPENIMAGEIO* -U *LLVM* -U *CYCLES* -U *OPENSUBDIV* -U *OPENVDB* -U *COLLADA* -U *FFMPEG* -U *ALEMBIC* -U *USD* -D WITH_CODEC_SNDFILE=ON -D PYTHON_VERSION=3.7 -D PYTHON_ROOT_DIR=/opt/lib/python-3.7 -D BOOST_ROOT=/opt/lib/boost -D Boost_NO_SYSTEM_PATHS=ON -D WITH_OPENCOLORIO=ON -D OPENCOLORIO_ROOT_DIR=/opt/lib/ocio -D OPENEXR_ROOT_DIR=/opt/lib/openexr -D WITH_OPENIMAGEIO=ON -D OPENIMAGEIO_ROOT_DIR=/opt/lib/oiio -D WITH_CYCLES_OSL=ON -D WITH_LLVM=ON -D LLVM_VERSION=9.0.1 -D OSL_ROOT_DIR=/opt/lib/osl -D LLVM_ROOT_DIR=/opt/lib/llvm -D LLVM_STATIC=ON -D WITH_OPENSUBDIV=ON -D OPENSUBDIV_ROOT_DIR=/opt/lib/osd -D WITH_ALEMBIC=ON -D ALEMBIC_ROOT_DIR=/opt/lib/alembic -D WITH_XR_OPENXR=ON -D XR_OPENXR_SDK_ROOT_DIR=/opt/lib/xr-openxr-sdk -D WITH_TBB=OFF -D WITH_CODEC_FFMPEG=OFF" bpy

RUN mkdir ~/bpy_lambda && \
    cd ~/bpy_lambda && \
    cp -R /opt/lib/python-3.7/lib/python3.7/site-packages/2.83 . && \
    cp -R ~/blender-git/build_linux_bpy/bin/bpy.so . && \
    cp -L /opt/lib/openexr-2.4.0/lib64/libHalf.so . && \
    cp -L /opt/lib/openexr-2.4.0/lib64/libIex.so . && \
    cp -L /opt/lib/openexr-2.4.0/lib64/libIlmImf.so . && \
    cp -L /opt/lib/openexr-2.4.0/lib64/libIlmThread.so . && \
    cp -L /opt/lib/openexr-2.4.0/lib64/libImath.so . && \
    cp -L /opt/lib/openexr-2.4.0/lib64/libIexMath-2_4.so.24 . && \
    cp -L /opt/lib/oiio-1.8.13/lib64/libOpenImageIO.so . && \
    cp -L /opt/lib/osd-3.4.0_RC2/lib/libosdGPU.so.3.4.0 . && \
    cp -L /opt/lib/osd-3.4.0_RC2/lib/libosdCPU.so.3.4.0 . && \
    cp -L /opt/lib/osl-1.10.9/lib64/liboslcomp.so.1.10 . && \
    cp -L /opt/lib/osl-1.10.9/lib64/liboslexec.so.1.10 . && \
    cp -L /opt/lib/osl-1.10.9/lib64/liboslquery.so.1.10 . && \
    cp -L /usr/lib64/libfftw3.so.3 . && \
    cp -L /usr/lib64/libopenjpeg.so.2 . && \
    cp -L /usr/lib64/libGLEW.so.2.2 . && \
    cp -L /opt/lib/boost-1.70.0/lib/libboost_chrono.so.1.70.0 . && \
    cp -L /opt/lib/boost-1.70.0/lib/libboost_date_time.so.1.70.0 . && \
    cp -L /opt/lib/boost-1.70.0/lib/libboost_filesystem.so.1.70.0 . && \
    cp -L /opt/lib/boost-1.70.0/lib/libboost_regex.so.1.70.0 . && \
    cp -L /opt/lib/boost-1.70.0/lib/libboost_system.so.1.70.0 . && \
    cp -L /opt/lib/boost-1.70.0/lib/libboost_thread.so.1.70.0 . && \
    cp -L /opt/lib/boost-1.70.0/lib/libboost_wave.so.1.70.0 . && \
    cp -L /opt/lib/python-3.7.4/lib/libpython3.7m.so.1.0 . && \
    cp -L /usr/lib64/libGLU.so.1 .

# Build artifact stored in /bpy_lambda
