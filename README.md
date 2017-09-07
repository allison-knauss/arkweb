# arkweb - Codebase for Allison's personal website

The plan is simple. An open source, MIT Licensed web application which serves as a home for some of my technical knowledge hosts my writing and public content, for which I retain proprietary ownership.

## Usage

You'll need docker. The application aims to be runable in docker by doing nothing more than `git clone https://github.com/allison-knauss/arkweb` followed by `docker-compose up`. Production deployments may require an extra step or two.

## Technology

- Python
- Flask
- PostgreSQL
- An as-yet-undetermined database migration library
- AngularJS or React
- HTML5

## Expectations

- All code will follow PEP-8 except the places I don't like it. If a different approach is distinctly cleaner, it's fine, except 4 space indentation is required at all times.
- 100% code unit test coverage. No excuses.
- All environments, including production, will eventually run Chaos Monkey.
- Code should be self-documenting. Use comments to clarify any pieces which aren't.

## Repository layout

- api/ contains all code for the api service
- web/ contains all code for the web service
- test/ contains all unit test code
