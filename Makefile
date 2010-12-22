help:
	@echo
	@echo "Please use 'make <user>' where <user> is a valid username."

clean:
	@echo "Cleaning..."
	@rm -rf build/

run:
	@echo "Running for ${user}..."
	python favtweets/favtweets.py ${user}