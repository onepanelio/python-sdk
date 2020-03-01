.DEFAULT_GOAL := sdk

init:
ifndef version
	err = $(error version is undefined)
	$(err)
endif
ifndef path
	err = $(error path is undefined)
	$(err)
endif
	mkdir -p .build
	cp $(path) .build/

sdk: init
	# generate sdk
	docker run --rm -v ${PWD}/.build:/build openapitools/openapi-generator-cli \
		generate -p packageName=onepanel.core.api,projectName=onepanel.core.api,packageVersion=$(version) -i /build/api.swagger.json -g python -o /build/
	rm .build/api.swagger.json
	
	# Update repository files with generated files
	cp -r .build/* .

	# Update generated files
	sed -i '' 's/git\+https:\/\/github.com\/GIT_USER_ID\/GIT_REPO_ID.git/onepanel-core/g' README.md