include .env
export

fetch:
	@read -p "Enter day number: " day; \
	if [ -z "$$day" ]; then \
		echo "Day number is required"; \
		exit 1; \
	fi; \
	url="https://adventofcode.com/2025/day/$$day/input"; \
	output="input/day$$day.txt"; \
	echo "Fetching input for day $$day..."; \
	curl -s -b "session=$$AOC_SESSION" "$$url" > "$$output" || { echo "Failed to fetch input. Make sure AOC_SESSION environment variable is set in .env file."; exit 1; }; \
	echo "Input saved to $$output"