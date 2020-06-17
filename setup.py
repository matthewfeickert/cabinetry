from setuptools import setup, find_packages

extras_require = {"contrib": ["matplotlib", "uproot", "scipy", "iminuit", "numexpr"]}
extras_require["test"] = sorted(
    set(
        extras_require["contrib"]
        + [
            "pytest",
            "pytest-cov>=2.5.1",
            "pydocstyle",
            "check-manifest",
            "flake8",
            "black;python_version>='3.6'",  # Black is Python3 only
        ]
    )
)
extras_require["develop"] = sorted(
    set(extras_require["test"] + ["pre-commit", "twine"])
)
extras_require["complete"] = sorted(set(sum(extras_require.values(), [])))


setup(extras_require=extras_require)
