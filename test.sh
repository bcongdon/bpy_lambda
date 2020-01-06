docker run --rm -u root -v "$PWD":/var/task:ro,delegated lambci/lambda:python3.6 test.handler
