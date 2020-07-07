rm bpy_lambda_layer.zip
mkdir package && mkdir package/python && mv bpy_lambda package/python/
cd package && zip -r9 ../bpy_lambda_layer.zip .
cd .. && mv ./package/python/bpy_lambda .
rmdir package/python && rmdir package
