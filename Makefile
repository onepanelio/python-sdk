.DEFAULT_GOAL := all

init:
ifndef version
	err = $(error version is undefined)
	$(err)
endif
ifndef path
	err = $(error path is undefined)
	$(err)
endif
	rm -rf .build
	mkdir -p .build
	cp $(path) .build/

sdk: init
	# generate sdk
	docker run --rm -v ${PWD}/.build:/build -v ${PWD}/openapi/templates:/onepanel openapitools/openapi-generator-cli:v4.3.1 \
		generate -p packageName=onepanel.core.api,projectName=onepanel-sdk,packageVersion=$(version) -t onepanel -i /build/api.swagger.json -g python -o /build/
	rm .build/api.swagger.json

	rm -rf ./docs ./onepanel/core .onepanel/__init__.py ./test setup.py setup.cfg test-requirements.txt tox.ini

	# Update repository files with generated files
	cp -r .build/* .
	rm -rf onepanel-core-sdk

publish-pip-package:
	python3 setup.py sdist
	twine upload dist/onepanel-sdk-$(version).tar.gz

all: sdk publish-pip-package