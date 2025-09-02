## Python

1. Package Management
    - I prefer to use uv for everything (uv add, uv run, etc)
    - Do not use old fashioned methods for package management like poetry, pip or easy_install.
    - Make sure that there is a pyproject.toml file in the root directory.
    - Use `uv sync --locked` for reproducible installs in CI/CD
    - Use `uv lock` to refresh lock file after dependency changes

2. Code Quality
    - Type hints required for all code
    - Functions must be focused and small
    - Follow existing patterns exactly
    - Line length: 80 chars maximum
    - use mypy for type checking:
        - run `uvx mypy` to start

3. Testing Requirements
    - Framework: `uv run pytest`
    - New features require tests
    - Bug fixes require regression tests

4. Code Formatting
    - Format: `uvx ruff format .`
    - Check: `uvx ruff check .`
    - Fix: `uvx ruff check . --fix`
    - Critical issues:
        - Line length (80 chars)
        - Import sorting (I001)
        - Use single line import
        - Unused imports

5. Code Style Guidelines
    - Use reStructuredText style docstring like this:
        ```
        """Explain the method.

        :param <param_name>: explain the parameter.
        :return: explain the return value.
        :raises: what may raise.
        """
        ```
    - Do NOT add param, return and raises doc for unittest test functions and methods.
    - Do not go too verbose in docstring.
    - Add detailed type hint where ever possible.
    - Use type hinting generics in standard collections. Avoid type hinting like `typing.List[int]`, use `list[int]` instead.
    - Do not violate PEP8 style guide.
    - Prefer aiohttp over requests and httpx.
    - Prefer Python 3.11 over other python version.
    - Prefer msgspec.Struct over TypedDict, dataclass and pydantic.BaseModel.
    - Do not import module inside function unless absolutely necessary.
    - If a variable name conflicts with a python keyword, add a "_" suffix to the variable name.


6. Pre-commit Workflow
    - Run quality checks before committing:
        1. `uvx ruff format .` (format code)
        2. `uvx ruff check . --fix` (fix linting issues)
        3. `uvx mypy` (type checking)
        4. `uv run pytest` (run tests)
    - Consider setting up pre-commit hooks for automatic checks
    - All checks must pass before pushing to remote

## IMPORTANT!
- Always ask agent python-code-specialist to do Python works.
- If the `.codemaker/rule/` directory exists in the project's root, read the files within it and follow the rules defined inside.