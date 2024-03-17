docker build -t "anicham-package-test" -f scripts/package-test.Dockerfile .
docker run -t anicham-package-test:latest