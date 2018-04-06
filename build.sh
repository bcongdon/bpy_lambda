echo "*** BUILDING bpy_lambda ***"
docker build -t bpy_lambda ./docker

echo "*** COPYING bpy_lambda ARTIFACTS ***"
docker run -d -it --name bpy_lambda bpy_lambda /bin/bash
docker cp bpy_lambda:/bpy_lambda .
cp shim/__init__.py ./bpy_lambda

echo "*** CLEANING UP ***"
docker kill bpy_lambda
docker rm bpy_lambda