# CHANGELOG


## v0.1.0 (2025-05-24)

### Bug Fixes

- Add coverage pragma comments for edge case handling in NameMother and TextMother
  ([`2fa0d81`](https://github.com/adriamontoto/object-mother-pattern/commit/2fa0d8115ea6a7ca0fe2942db3fb774365e766a9))

- Add coverage pragma comments for list, set, tuple, dict, and datetime types in BaseMother class
  ([`1a981df`](https://github.com/adriamontoto/object-mother-pattern/commit/1a981df1746c5b71bd5f62f88254a2b0b81e629a))

- Add coverage pragma comments in DatetimeMother and NameMother for clarity
  ([`13987bd`](https://github.com/adriamontoto/object-mother-pattern/commit/13987bda5528189424218501b17ae8c254083589))

- Fix lint and coverage returning errors
  ([`a7b14e6`](https://github.com/adriamontoto/object-mother-pattern/commit/a7b14e6bd100fe5c2f38f4fdb52e0cbfd16ee532))

Signed-off-by: Adria Montoto <75563346+adriamontoto@users.noreply.github.com>

- Fix number of decimals when generating a float value
  ([`17a4c7c`](https://github.com/adriamontoto/object-mother-pattern/commit/17a4c7cbc8e312102db0e8050003a8b3730acc7e))

- Implement timezone awareness to DatetimeMother
  ([`a5975d0`](https://github.com/adriamontoto/object-mother-pattern/commit/a5975d072b3789d8893849490e75d45dbfa3745f))

- Improve error messages and handle edge cases in FloatMother
  ([`b9655a5`](https://github.com/adriamontoto/object-mother-pattern/commit/b9655a5ad99b3bf29d5a166936d87abbae6b1050))

- Remove invalid type NoneType
  ([`75d6bb8`](https://github.com/adriamontoto/object-mother-pattern/commit/75d6bb81db6745c202fc9ece0d58d1ec2b8b169e))

- Streamline FloatMother to handle equal min and max values correctly
  ([`993c203`](https://github.com/adriamontoto/object-mother-pattern/commit/993c203b48a8872fbc6ecc38128d7a8d82943af7))

- Update bug template
  ([`48e6b58`](https://github.com/adriamontoto/object-mother-pattern/commit/48e6b587f0751eb4e96d543dce8d6effd9d8f457))

- Update float mother tests to allow zero values
  ([`447c34d`](https://github.com/adriamontoto/object-mother-pattern/commit/447c34dc4d4febdc9f17dd71b51bc86e50a7414f))

- Update import paths for StringMother in StringUuidMother and MacAddressMother
  ([`129e1d0`](https://github.com/adriamontoto/object-mother-pattern/commit/129e1d022d971bc5f672a237bbeeac23e3a51e84))

- Update python-dateutil dependency upper bound to <3.0.0
  ([`17084a2`](https://github.com/adriamontoto/object-mother-pattern/commit/17084a2dce8a7253097ae2b520ad3f48a9c3933c))

- Update StringDatetimeMother tests to use DatetimeMother for invalid type checks
  ([`4c6780b`](https://github.com/adriamontoto/object-mother-pattern/commit/4c6780b2530422ecc450c7ed69957d974b35b19e))

- **out of range**: Fix out of range method by adding an epsilon to the range
  ([`e3aa831`](https://github.com/adriamontoto/object-mother-pattern/commit/e3aa8312e7ecdbda73063ec815fdc97e68ec4f0e))

Signed-off-by: Adria Montoto <75563346+adriamontoto@users.noreply.github.com>

- **tests**: Ensure positive min_length in PasswordMother random_length tests
  ([`c7a5336`](https://github.com/adriamontoto/object-mother-pattern/commit/c7a5336c9207491a49ea55e2d90246332e5bab11))

Updated PasswordMother random_length test cases to use IntegerMother.positive() for min_length
  parameter, ensuring it's always a positive number. This aligns with the expected behavior of the
  random_length method.

Signed-off-by: Adria Montoto <75563346+adriamontoto@users.noreply.github.com>

### Build System

- Add new dependencies to the package
  ([`9a69232`](https://github.com/adriamontoto/object-mother-pattern/commit/9a692320a9f2bdc2f174a31e86ad7088a26e432f))

Signed-off-by: Adria Montoto <75563346+adriamontoto@users.noreply.github.com>

- Create version 2024.12.21
  ([`9d6c326`](https://github.com/adriamontoto/object-mother-pattern/commit/9d6c32630a0bae1ed4733a45c8358daf7ac761d4))

- Make package versions more permissible
  ([`d97a13f`](https://github.com/adriamontoto/object-mother-pattern/commit/d97a13f7105a4b61c41cb35e27baa304df32c328))

Signed-off-by: Adria Montoto <75563346+adriamontoto@users.noreply.github.com>

- Remove linting error when removing noqa comments
  ([`0bbb523`](https://github.com/adriamontoto/object-mother-pattern/commit/0bbb523cd00461ac9009db572d01fc0c7f3cbcd3))

Signed-off-by: Adria Montoto <75563346+adriamontoto@users.noreply.github.com>

- Remove pytest-asyncio from development requirements
  ([`510c093`](https://github.com/adriamontoto/object-mother-pattern/commit/510c09357739c6148b27b11fbdb70ab78e9d600a))

- Simplify .gitignore file
  ([`bf8800f`](https://github.com/adriamontoto/object-mother-pattern/commit/bf8800fbc95bca0e5b082a45328b87591b74d800))

Signed-off-by: Adria Montoto <75563346+adriamontoto@users.noreply.github.com>

- Simplify .gitignore file
  ([`7205927`](https://github.com/adriamontoto/object-mother-pattern/commit/72059274ae32d4eb2b02ab36d7085390580772f6))

Signed-off-by: Adria Montoto <75563346+adriamontoto@users.noreply.github.com>

- Update .gitignore to exclude all coverage files
  ([`b0af1a1`](https://github.com/adriamontoto/object-mother-pattern/commit/b0af1a16cea1954c5959fc5ad65dbb55af72f829))

- Update .gitignore to exclude coverage and environment folders
  ([`ed21e12`](https://github.com/adriamontoto/object-mother-pattern/commit/ed21e1204e33c5637cf43457c3fb08f48c30f7ff))

- Update faker requirement
  ([`0ca9ee3`](https://github.com/adriamontoto/object-mother-pattern/commit/0ca9ee3277d872bcdfdb1d2dc569867d4afb6182))

Updates the requirements on [faker](https://github.com/joke2k/faker) to permit the latest version. -
  [Release notes](https://github.com/joke2k/faker/releases) -
  [Changelog](https://github.com/joke2k/faker/blob/master/CHANGELOG.md) -
  [Commits](https://github.com/joke2k/faker/compare/v29.0.0...v37.0.0)

--- updated-dependencies: - dependency-name: faker dependency-type: direct:production ...

Signed-off-by: dependabot[bot] <support@github.com>

### Chores

- Correct typo in .gitignore comment for clarity
  ([`200b139`](https://github.com/adriamontoto/object-mother-pattern/commit/200b13922794150e4a32c70bf184eca85aa80c6f))

- Remove main.py file
  ([`17d00e6`](https://github.com/adriamontoto/object-mother-pattern/commit/17d00e6246adaee4b51d08543a36c31390264aa7))

Signed-off-by: Adria Montoto <75563346+adriamontoto@users.noreply.github.com>

- Remove unused name and text mothers
  ([`460ceda`](https://github.com/adriamontoto/object-mother-pattern/commit/460ceda2333d5c7c897a2c77649c13ff50e40305))

- Update comments in .gitignore for clarity and consistency
  ([`559c82b`](https://github.com/adriamontoto/object-mother-pattern/commit/559c82b8d8c1ac6f429dec351302252c36db28b1))

- Update license reference in pyproject.toml to point to LICENSE.md
  ([`eda446a`](https://github.com/adriamontoto/object-mother-pattern/commit/eda446ae1d9d16abc5c62e0cb05ef19ae40e2b1a))

- Update license reference in pyproject.toml to point to LICENSE.md
  ([`ea0586f`](https://github.com/adriamontoto/object-mother-pattern/commit/ea0586f0cbce35bb41a8869cc0a5222092a691b1))

- Update version to 2025.01.03
  ([`f6e38c2`](https://github.com/adriamontoto/object-mother-pattern/commit/f6e38c27bc3482b2101a8c727cc0b9f332e32b36))

- Update version to 2025.01.12
  ([`c1d77f0`](https://github.com/adriamontoto/object-mother-pattern/commit/c1d77f05afcbd594867e4e166a4023b3d58dd2bb))

### Continuous Integration

- Add a setup makefile command to setup the project
  ([`fa6fc66`](https://github.com/adriamontoto/object-mother-pattern/commit/fa6fc668ac1d70372c9a4c6a19652bf81acacb1f))

Signed-off-by: Adria Montoto <75563346+adriamontoto@users.noreply.github.com>

- Add commit message checker
  ([`330dffc`](https://github.com/adriamontoto/object-mother-pattern/commit/330dffc111ce91145bfeedc3b9051c60222f6db6))

Signed-off-by: Adria Montoto <75563346+adriamontoto@users.noreply.github.com>

- Bump actions/cache from 4.2.0 to 4.2.2
  ([`e2ef753`](https://github.com/adriamontoto/object-mother-pattern/commit/e2ef7533810a93ccad237c79e4344d78371ce9c4))

Bumps [actions/cache](https://github.com/actions/cache) from 4.2.0 to 4.2.2. - [Release
  notes](https://github.com/actions/cache/releases) -
  [Changelog](https://github.com/actions/cache/blob/main/RELEASES.md) -
  [Commits](https://github.com/actions/cache/compare/v4.2.0...v4.2.2)

--- updated-dependencies: - dependency-name: actions/cache dependency-type: direct:production

update-type: version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>

- Bump actions/cache from 4.2.2 to 4.2.3
  ([`72f8680`](https://github.com/adriamontoto/object-mother-pattern/commit/72f86801773bb18c56f7e46165d469edd104de18))

Bumps [actions/cache](https://github.com/actions/cache) from 4.2.2 to 4.2.3. - [Release
  notes](https://github.com/actions/cache/releases) -
  [Changelog](https://github.com/actions/cache/blob/main/RELEASES.md) -
  [Commits](https://github.com/actions/cache/compare/v4.2.2...v4.2.3)

--- updated-dependencies: - dependency-name: actions/cache dependency-type: direct:production

update-type: version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>

- Bump actions/download-artifact from 4.1.8 to 4.1.9
  ([`169eec6`](https://github.com/adriamontoto/object-mother-pattern/commit/169eec6d9b3db07e87cce20fa5111f7c9eff9f74))

Bumps [actions/download-artifact](https://github.com/actions/download-artifact) from 4.1.8 to 4.1.9.
  - [Release notes](https://github.com/actions/download-artifact/releases) -
  [Commits](https://github.com/actions/download-artifact/compare/v4.1.8...v4.1.9)

--- updated-dependencies: - dependency-name: actions/download-artifact dependency-type:
  direct:production

update-type: version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>

- Bump actions/download-artifact from 4.1.9 to 4.2.1
  ([`ae05daf`](https://github.com/adriamontoto/object-mother-pattern/commit/ae05dafb3790ff88896da4b23c714beb1a8fc7e7))

Bumps [actions/download-artifact](https://github.com/actions/download-artifact) from 4.1.9 to 4.2.1.
  - [Release notes](https://github.com/actions/download-artifact/releases) -
  [Commits](https://github.com/actions/download-artifact/compare/v4.1.9...v4.2.1)

--- updated-dependencies: - dependency-name: actions/download-artifact dependency-type:
  direct:production

update-type: version-update:semver-minor ...

Signed-off-by: dependabot[bot] <support@github.com>

- Bump actions/download-artifact from 4.2.1 to 4.3.0
  ([#38](https://github.com/adriamontoto/object-mother-pattern/pull/38),
  [`0047fd4`](https://github.com/adriamontoto/object-mother-pattern/commit/0047fd481f8c6668c8fd8a296dcca319768f5053))

Signed-off-by: dependabot[bot] <support@github.com>

Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>

- Bump actions/setup-python from 5.3.0 to 5.4.0
  ([`20efed2`](https://github.com/adriamontoto/object-mother-pattern/commit/20efed2c940d8fdfcb8f907314ae7817a4848ec4))

Bumps [actions/setup-python](https://github.com/actions/setup-python) from 5.3.0 to 5.4.0. -
  [Release notes](https://github.com/actions/setup-python/releases) -
  [Commits](https://github.com/actions/setup-python/compare/v5.3.0...v5.4.0)

--- updated-dependencies: - dependency-name: actions/setup-python dependency-type: direct:production

update-type: version-update:semver-minor ...

Signed-off-by: dependabot[bot] <support@github.com>

- Bump actions/setup-python from 5.4.0 to 5.5.0
  ([#31](https://github.com/adriamontoto/object-mother-pattern/pull/31),
  [`da59c0f`](https://github.com/adriamontoto/object-mother-pattern/commit/da59c0f9aa3ab60baa43ae199fbabf2e52ea91ee))

Signed-off-by: dependabot[bot] <support@github.com>

Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>

- Bump actions/setup-python from 5.5.0 to 5.6.0
  ([#37](https://github.com/adriamontoto/object-mother-pattern/pull/37),
  [`4ac4ebe`](https://github.com/adriamontoto/object-mother-pattern/commit/4ac4ebe08d6b3556ca26720b4ae7e1996601d200))

Signed-off-by: dependabot[bot] <support@github.com>

Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>

- Bump actions/upload-artifact from 4.5.0 to 4.6.0
  ([`035a6a9`](https://github.com/adriamontoto/object-mother-pattern/commit/035a6a912077c6656270553e62fa26a8ee68c67c))

Bumps [actions/upload-artifact](https://github.com/actions/upload-artifact) from 4.5.0 to 4.6.0. -
  [Release notes](https://github.com/actions/upload-artifact/releases) -
  [Commits](https://github.com/actions/upload-artifact/compare/v4.5.0...v4.6.0)

--- updated-dependencies: - dependency-name: actions/upload-artifact dependency-type:
  direct:production

update-type: version-update:semver-minor ...

Signed-off-by: dependabot[bot] <support@github.com>

- Bump actions/upload-artifact from 4.6.0 to 4.6.1
  ([`b5214f0`](https://github.com/adriamontoto/object-mother-pattern/commit/b5214f07252f2df19cda0e4de00228684f241e1b))

Bumps [actions/upload-artifact](https://github.com/actions/upload-artifact) from 4.6.0 to 4.6.1. -
  [Release notes](https://github.com/actions/upload-artifact/releases) -
  [Commits](https://github.com/actions/upload-artifact/compare/v4.6.0...v4.6.1)

--- updated-dependencies: - dependency-name: actions/upload-artifact dependency-type:
  direct:production

update-type: version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>

- Bump actions/upload-artifact from 4.6.1 to 4.6.2
  ([`87ec6a9`](https://github.com/adriamontoto/object-mother-pattern/commit/87ec6a968c495069333886d7887364a06e3dc510))

Bumps [actions/upload-artifact](https://github.com/actions/upload-artifact) from 4.6.1 to 4.6.2. -
  [Release notes](https://github.com/actions/upload-artifact/releases) -
  [Commits](https://github.com/actions/upload-artifact/compare/v4.6.1...v4.6.2)

--- updated-dependencies: - dependency-name: actions/upload-artifact dependency-type:
  direct:production

update-type: version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>

- Bump github/codeql-action from 3.27.9 to 3.28.1
  ([`e819c8b`](https://github.com/adriamontoto/object-mother-pattern/commit/e819c8bd267ea9a5f0559d4fad5c414b44079e68))

Bumps [github/codeql-action](https://github.com/github/codeql-action) from 3.27.9 to 3.28.1. -
  [Release notes](https://github.com/github/codeql-action/releases) -
  [Changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md) -
  [Commits](https://github.com/github/codeql-action/compare/v3.27.9...v3.28.1)

--- updated-dependencies: - dependency-name: github/codeql-action dependency-type: direct:production

update-type: version-update:semver-minor ...

Signed-off-by: dependabot[bot] <support@github.com>

- Bump github/codeql-action from 3.28.1 to 3.28.11
  ([`90fc114`](https://github.com/adriamontoto/object-mother-pattern/commit/90fc114234ffe9d10da383431fd3c759e329fc38))

Bumps [github/codeql-action](https://github.com/github/codeql-action) from 3.28.1 to 3.28.11. -
  [Release notes](https://github.com/github/codeql-action/releases) -
  [Changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md) -
  [Commits](https://github.com/github/codeql-action/compare/v3.28.1...v3.28.11)

--- updated-dependencies: - dependency-name: github/codeql-action dependency-type: direct:production

update-type: version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>

- Bump github/codeql-action from 3.28.11 to 3.28.12
  ([`e5e1a08`](https://github.com/adriamontoto/object-mother-pattern/commit/e5e1a087e2cd0dc89a128a32505244643e9a0d3d))

Bumps [github/codeql-action](https://github.com/github/codeql-action) from 3.28.11 to 3.28.12. -
  [Release notes](https://github.com/github/codeql-action/releases) -
  [Changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md) -
  [Commits](https://github.com/github/codeql-action/compare/v3.28.11...v3.28.12)

--- updated-dependencies: - dependency-name: github/codeql-action dependency-type: direct:production

update-type: version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>

- Bump github/codeql-action from 3.28.12 to 3.28.15
  ([#32](https://github.com/adriamontoto/object-mother-pattern/pull/32),
  [`6f84f94`](https://github.com/adriamontoto/object-mother-pattern/commit/6f84f94b0c7e961cb2cd2397ccd6865918c89b77))

Signed-off-by: dependabot[bot] <support@github.com>

Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>

- Bump github/codeql-action from 3.28.15 to 3.28.17
  ([#39](https://github.com/adriamontoto/object-mother-pattern/pull/39),
  [`64efe2b`](https://github.com/adriamontoto/object-mother-pattern/commit/64efe2bc1186a478bc627eb736445fddb54e2c1b))

Signed-off-by: dependabot[bot] <support@github.com>

Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>

- Bump pypa/gh-action-pypi-publish from 1.12.3 to 1.12.4
  ([`796ef8c`](https://github.com/adriamontoto/object-mother-pattern/commit/796ef8cbb16d316c939da60eb032bbcf72a63a0e))

Bumps [pypa/gh-action-pypi-publish](https://github.com/pypa/gh-action-pypi-publish) from 1.12.3 to
  1.12.4. - [Release notes](https://github.com/pypa/gh-action-pypi-publish/releases) -
  [Commits](https://github.com/pypa/gh-action-pypi-publish/compare/v1.12.3...v1.12.4)

--- updated-dependencies: - dependency-name: pypa/gh-action-pypi-publish dependency-type:
  direct:production

update-type: version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>

- Implement build makefile command
  ([`5c53268`](https://github.com/adriamontoto/object-mother-pattern/commit/5c5326844995d98f6b30e6bbd86543370b5b33fe))

Signed-off-by: Adria Montoto <75563346+adriamontoto@users.noreply.github.com>

- Release pipeline workflow
  ([`90afd78`](https://github.com/adriamontoto/object-mother-pattern/commit/90afd7856aa65834dc8596ae57eb8145b7837b3f))

Signed-off-by: Adria Montoto <75563346+adriamontoto@users.noreply.github.com>

- Remove JSON files checker from pre-commit configuration
  ([`418f1d2`](https://github.com/adriamontoto/object-mother-pattern/commit/418f1d266c95ccc3c7184f527c80a9161c455ae8))

- Simplify pre commit configuration file
  ([`470ad5c`](https://github.com/adriamontoto/object-mother-pattern/commit/470ad5c5291df3d2df8e8e9cd5180919e9d3138e))

Signed-off-by: Adria Montoto <75563346+adriamontoto@users.noreply.github.com>

- Update dependabot commit emoji
  ([`b33b223`](https://github.com/adriamontoto/object-mother-pattern/commit/b33b22376e6e8004a8dbcb32039bbea997997682))

Signed-off-by: Adria Montoto <75563346+adriamontoto@users.noreply.github.com>

- Update gitleaks version
  ([`deff2a7`](https://github.com/adriamontoto/object-mother-pattern/commit/deff2a79290cdd168f8e24b441834c9c33156d7c))

Signed-off-by: Adria Montoto <75563346+adriamontoto@users.noreply.github.com>

- Update makefile with new constants
  ([`2af2895`](https://github.com/adriamontoto/object-mother-pattern/commit/2af28952b087a5efefcebe8d69b86527a448b857))

Signed-off-by: Adria Montoto <75563346+adriamontoto@users.noreply.github.com>

- Update the makefiles and pipelines to work with new makefile optimizations
  ([`e54c0fc`](https://github.com/adriamontoto/object-mother-pattern/commit/e54c0fc194ca9d1305adf60f672018741fb845b4))

Signed-off-by: Adria Montoto <75563346+adriamontoto@users.noreply.github.com>

- Use fixed hashes versions for github actions
  ([`e933dbe`](https://github.com/adriamontoto/object-mother-pattern/commit/e933dbe2e65b3cae8139799430e24efd47a6b018))

Signed-off-by: Adria Montoto <75563346+adriamontoto@users.noreply.github.com>

- Use fixed hashes versions for pre-commit
  ([`de58150`](https://github.com/adriamontoto/object-mother-pattern/commit/de58150aac398b261ac98e99dab1f392077392fc))

Signed-off-by: Adria Montoto <75563346+adriamontoto@users.noreply.github.com>

- Use makefile commands in all workflows
  ([`97a3b1f`](https://github.com/adriamontoto/object-mother-pattern/commit/97a3b1f0f51e349f7260238f0158516e808ab5e5))

Signed-off-by: Adria Montoto <75563346+adriamontoto@users.noreply.github.com>

### Documentation

- Add contributing guidelines to README
  ([`71c6f72`](https://github.com/adriamontoto/object-mother-pattern/commit/71c6f72b4145681131cbdf99ff18ed4c14dcc8b0))

- Add usage examples to FullNameMother and UsernameMother classes
  ([`1c164df`](https://github.com/adriamontoto/object-mother-pattern/commit/1c164df8e9c1ce5d521d1b744651b05790d482ef))

- Add utilization section with examples and real-life case for Object Mother library
  ([`54a2283`](https://github.com/adriamontoto/object-mother-pattern/commit/54a22834e957d52d7cd30ed1da8bc0d365153739))

- Enhance documentation for boolean, bytes, float, and integer mothers
  ([`b2c3711`](https://github.com/adriamontoto/object-mother-pattern/commit/b2c37110aea8cba58a4eac3285deeb92015fdd4f))

- Enhance documentation for date, datetime and uuid mothers
  ([`eb358b5`](https://github.com/adriamontoto/object-mother-pattern/commit/eb358b505bef2c6d9fdf5867d56c39c714dc96db))

- Refine docstring for MacAddressMother class
  ([`717cefc`](https://github.com/adriamontoto/object-mother-pattern/commit/717cefc4f5a96514fc8d1168fd68e6e5ba64e01d))

- Update example outputs in README and BytesMother, StringMother classes for consistency
  ([`96d7fe5`](https://github.com/adriamontoto/object-mother-pattern/commit/96d7fe5cf83b64673614e4446f5e6bf8e30d7b5f))

- Update makefile help command
  ([`6e9d015`](https://github.com/adriamontoto/object-mother-pattern/commit/6e9d01533c644b541c6cb543f041502255fbc665))

Signed-off-by: Adria Montoto <75563346+adriamontoto@users.noreply.github.com>

### Features

- Add BoolMother class for generating random boolean values
  ([`e5fae0e`](https://github.com/adriamontoto/object-mother-pattern/commit/e5fae0eae347953e9e30853728ba3a5deb1f2c06))

- Add echos to print the status of the command in makefile
  ([`05c2363`](https://github.com/adriamontoto/object-mother-pattern/commit/05c23638f2f82bb0a65d358cd97f586c96de793b))

Signed-off-by: Adria Montoto <75563346+adriamontoto@users.noreply.github.com>

- Add IntegerMother class for generating random integers
  ([`dabe2fc`](https://github.com/adriamontoto/object-mother-pattern/commit/dabe2fc8272dfc5cfccbf0a22e5d31ddb8b01fbe))

- Add invalid_value method to StringDateMother and StringDatetimeMother classes
  ([`b11b645`](https://github.com/adriamontoto/object-mother-pattern/commit/b11b645d4133903bb4abee541077cc4b017ddc8c))

- Add TLD domains list
  ([`b0713b2`](https://github.com/adriamontoto/object-mother-pattern/commit/b0713b209bc4e7b6f93c378480cfa4c4b3677197))

- Create alias for install dev dependencies and execute tests
  ([`ec2f9d1`](https://github.com/adriamontoto/object-mother-pattern/commit/ec2f9d1d1f476c6fa677da4e63f7f307f3410339))

Signed-off-by: Adria Montoto <75563346+adriamontoto@users.noreply.github.com>

- Enhance words list retrieval by filtering out comments and empty lines; update file modification
  timestamp
  ([`ea990cf`](https://github.com/adriamontoto/object-mother-pattern/commit/ea990cfb1812178297c2bfe9fabed7feb09d1fd0))

- First commit :D
  ([`11f12a5`](https://github.com/adriamontoto/object-mother-pattern/commit/11f12a59075587f3a3031859841b5b018a947e7a))

- Implement a script to update list of the packages
  ([`ae7b962`](https://github.com/adriamontoto/object-mother-pattern/commit/ae7b96286c0692ca579bec18376f1e158b650116))

- Implement AWS cloud regions retrieval and local update functionality
  ([`423f0af`](https://github.com/adriamontoto/object-mother-pattern/commit/423f0af13e7eaebb5ba899b1206e9cfbcc32d24a))

- Implement AwsCloudRegionMother for generating random AWS cloud region values
  ([`93fac91`](https://github.com/adriamontoto/object-mother-pattern/commit/93fac91fbd173923ec7f14cdc95b5628a43bc418))

- Implement base mother
  ([`e9a56da`](https://github.com/adriamontoto/object-mother-pattern/commit/e9a56da55b374504a01830fb1099ce1bf959d8bf))

- Implement BtcWalletMother for generating random BTC wallet addresses
  ([`107f43f`](https://github.com/adriamontoto/object-mother-pattern/commit/107f43f283004d10d5e4fb13f7ba8b0d257bff6a))

- Implement BytesMother
  ([`7a9504e`](https://github.com/adriamontoto/object-mother-pattern/commit/7a9504edadf36b6fe653217fcadbd699978a87f2))

- Implement Date and Datetime mothers with corresponding tests
  ([`a5e20c3`](https://github.com/adriamontoto/object-mother-pattern/commit/a5e20c3e161d19e2e8d90be9021726089c3046cb))

- Implement EnumerationMother for generating random enum values of the given enumeration
  ([`97d2f9d`](https://github.com/adriamontoto/object-mother-pattern/commit/97d2f9dc98bcf7027c26bc7bfa27f86b2baff3c6))

- Implement FloatMother class for generating random float values
  ([`9b2dafc`](https://github.com/adriamontoto/object-mother-pattern/commit/9b2dafc5aa45b5e37c90aa7f6eafc3af42c01e05))

- Implement FullNameMother and UsernameMother for generating random names and usernames
  ([`e82f4d4`](https://github.com/adriamontoto/object-mother-pattern/commit/e82f4d48c37fca4ddd8e8c9576f19c96620966c1))

- Implement Ipv4, Ipv6 network and address mothers for random value generation
  ([`32aec20`](https://github.com/adriamontoto/object-mother-pattern/commit/32aec20809fd438dde74368eeb710823680b55f0))

- Implement MacAddressMother for generating random MAC addresses
  ([`bd4e60f`](https://github.com/adriamontoto/object-mother-pattern/commit/bd4e60f2faac70d3a4f707520700506d67fa8f4f))

- Implement NameMother class for generating random name values
  ([`b44eb93`](https://github.com/adriamontoto/object-mother-pattern/commit/b44eb93eb3f7ccec5e3db35fdf5596c9751cdca4))

- Implement out_of_range method to FloatMother and IntegerMother
  ([`782f0f0`](https://github.com/adriamontoto/object-mother-pattern/commit/782f0f0f5de7ca5b8589afecbde66c6b5f0177d9))

- Implement positive_or_zero and negative_or_zero methods in IntegerMother
  ([`a5a7eb6`](https://github.com/adriamontoto/object-mother-pattern/commit/a5a7eb64c0b26e83418c31111740e604e539deac))

- Implement StringMother class for generating random string values
  ([`aaf92fa`](https://github.com/adriamontoto/object-mother-pattern/commit/aaf92fa8d89a28f6c6f7557e8ad88ded9f6833fe))

- Implement StringUUIDMother and UUIDMother classes with corresponding tests
  ([`bc02a5c`](https://github.com/adriamontoto/object-mother-pattern/commit/bc02a5cfde314087c87a73f6527d3d1bcd75a2fa))

- Implement TextMother class for generating random text values
  ([`212f61d`](https://github.com/adriamontoto/object-mother-pattern/commit/212f61dbc39c171cb5a606772204daa91c9ef72a))

- Implement true and false methods to BooleanMother
  ([`b9b5990`](https://github.com/adriamontoto/object-mother-pattern/commit/b9b59903ef6c56b4e7f5cf767c491f0c4059cca1))

- Random choose the case for btc wallets
  ([`9c8eb4b`](https://github.com/adriamontoto/object-mother-pattern/commit/9c8eb4be8f6d45374070fc0d271102fb07b0fe0b))

- Remove stdout outputs when not using VERBOSE=true
  ([`0301cf4`](https://github.com/adriamontoto/object-mother-pattern/commit/0301cf4cf620db391c36cdb16a2febabac665a3a))

Signed-off-by: Adria Montoto <75563346+adriamontoto@users.noreply.github.com>

- Simplify float mother api
  ([`a6b0d15`](https://github.com/adriamontoto/object-mother-pattern/commit/a6b0d15ccfdfb33a571a497f6ebf3ffa39d1203a))

Signed-off-by: Adria Montoto <75563346+adriamontoto@users.noreply.github.com>

- Simplify string mother api
  ([`69229ba`](https://github.com/adriamontoto/object-mother-pattern/commit/69229ba2015cd2c60f102a10527b95bfc5ffdd76))

Signed-off-by: Adria Montoto <75563346+adriamontoto@users.noreply.github.com>

- Update FloatMother to allow random decimal places when not specified
  ([`c0aff1b`](https://github.com/adriamontoto/object-mother-pattern/commit/c0aff1bcf20d33456622ac7273a6ac2bd1a41075))

- **aws regions**: Add invalid_value method to AwsCloudRegionMother and tests
  ([`8d49b96`](https://github.com/adriamontoto/object-mother-pattern/commit/8d49b969441a9ac8daccdf3dbf95d1550494f642))

- **identifiers**: Add Spanish DNI Mother implementation
  ([`23a8d58`](https://github.com/adriamontoto/object-mother-pattern/commit/23a8d58895c9db4f0140fef5d58ed9b56493e539))

Add DniMother class for Spanish National Identity Document validation and generation: - Implement
  regex validation for DNI format (8 digits + check letter) - Add check letter algorithm based on
  the Spanish DNI standard - Support both uppercase and lowercase letter formats via DniCase enum -
  Create comprehensive test suite with validation tests - Organize in proper country-specific
  package structure

The implementation follows the Object Mother pattern and project standards.

- **identifiers**: Implement nie mother
  ([`511c954`](https://github.com/adriamontoto/object-mother-pattern/commit/511c954ebb301d13c6060586711a433fd0bd3b00))

Signed-off-by: Adria Montoto <75563346+adriamontoto@users.noreply.github.com>

- **people**: Implement password mother
  ([`ea9c711`](https://github.com/adriamontoto/object-mother-pattern/commit/ea9c711291ecf6c8d41c4fa16b7371af6a8144ae))

Signed-off-by: Adria Montoto <75563346+adriamontoto@users.noreply.github.com>

### Performance Improvements

- Improve boolean mother performance
  ([`d4c23e3`](https://github.com/adriamontoto/object-mother-pattern/commit/d4c23e3be2ab167bb3b36e31a860008249bdd26c))

- Improve bytes mother performance
  ([`599e21b`](https://github.com/adriamontoto/object-mother-pattern/commit/599e21bcdc2881abc10fa410a2105919a76a7698))

- Improve float mother performance
  ([`eeed82e`](https://github.com/adriamontoto/object-mother-pattern/commit/eeed82ed663d4ff2283f6f6d8d57c9c9091f8ba0))

- Improve integer mother performance
  ([`bcf94fc`](https://github.com/adriamontoto/object-mother-pattern/commit/bcf94fca14c6aa596ca8f7c0dec6ec25ee850739))

- Improve string mother performance and implement new methods
  ([`a4b1c45`](https://github.com/adriamontoto/object-mother-pattern/commit/a4b1c453d40800c506fc032598a0859ca21e2652))

- Improve uuid mothers performance
  ([`0ea25b7`](https://github.com/adriamontoto/object-mother-pattern/commit/0ea25b70b5ffd3e6cd4eb952dd3fac8ca0e5ed2f))

### Refactoring

- Change mixed enums to mixedcase
  ([`cf648f3`](https://github.com/adriamontoto/object-mother-pattern/commit/cf648f364bd297cda35ae0060291a479171539b5))

Signed-off-by: Adria Montoto <75563346+adriamontoto@users.noreply.github.com>

- Improve type checking for value parameters in various Mother classes
  ([`81758af`](https://github.com/adriamontoto/object-mother-pattern/commit/81758afcaa6dfb28f2167152b5b7d12b083691a3))

- Move primitives tests to primitives test folder
  ([`79b280b`](https://github.com/adriamontoto/object-mother-pattern/commit/79b280b5cb496eb401ad1901a136dfc6f7ed9754))

- Remove redundant type and value checks in IntegerMother
  ([`d27e785`](https://github.com/adriamontoto/object-mother-pattern/commit/d27e7855a8cf6ebed350ba1055feebcb9752faec))

- Rename BoolMother to BooleanMother for consistency and clarity
  ([`7b45e58`](https://github.com/adriamontoto/object-mother-pattern/commit/7b45e5822c622a8e2012f6003a48e66e718f0cd1))

- Reorganize BoolMother and IntegerMother into primitives directory
  ([`8432c70`](https://github.com/adriamontoto/object-mother-pattern/commit/8432c701a1b6302fcd51ed06801a6b961357435d))

- Reorganize mother classes into date and identifier modules, update naming conventions
  ([`0e0562d`](https://github.com/adriamontoto/object-mother-pattern/commit/0e0562dcff696e8c629580c407616bd66a5015ab))

- Replace string 'invalid' with IntegerMother.invalid_type() in IntegerMother tests
  ([`e15e763`](https://github.com/adriamontoto/object-mother-pattern/commit/e15e7630878198d6772b266f9f547fe45dfec48a))

- Run automatic formatter
  ([`d5cc05e`](https://github.com/adriamontoto/object-mother-pattern/commit/d5cc05ea76ab26c49e37731ffd69e717acf9ceb1))

Signed-off-by: github-actions <41898282+github-actions[bot]@users.noreply.github.com>

- Suppress ruff warning for choice function in BaseMother
  ([`9deb714`](https://github.com/adriamontoto/object-mother-pattern/commit/9deb7145bd6d260179ff3eb966e81d150222b634))

- Update date generation method
  ([`948f509`](https://github.com/adriamontoto/object-mother-pattern/commit/948f509ff9fd7062648483dbf0c1852944516d4d))

- Update import of override for compatibility with Python 3.11
  ([`56cc194`](https://github.com/adriamontoto/object-mother-pattern/commit/56cc1941b29189f0f4d4df3ce03f1e7a0761ce8f))

- Update import paths for consistency across mother classes
  ([`68fc91f`](https://github.com/adriamontoto/object-mother-pattern/commit/68fc91fbadcbc4a5d919f6c19ebff53e21e17857))

### Testing

- Add unit test mark to the tests
  ([`7919a10`](https://github.com/adriamontoto/object-mother-pattern/commit/7919a10cc2515aebeaa934be896f30ea69e1327b))

- Completestring mother tests
  ([`9492c86`](https://github.com/adriamontoto/object-mother-pattern/commit/9492c8678148d3318840b2929827f818e77315ba))

Signed-off-by: Adria Montoto <75563346+adriamontoto@users.noreply.github.com>

- Implementtest modules for BytesMother, StringMother, FloatMother
  ([`d27db3b`](https://github.com/adriamontoto/object-mother-pattern/commit/d27db3be9baa775b88af458427107f813374140b))

- Improveboolean mother tests documentation
  ([`201d75e`](https://github.com/adriamontoto/object-mother-pattern/commit/201d75effc8762531fc01ab84be53c57e613b1d6))

Signed-off-by: Adria Montoto <75563346+adriamontoto@users.noreply.github.com>

- Improvebytes mother reliability
  ([`d9e2bf5`](https://github.com/adriamontoto/object-mother-pattern/commit/d9e2bf5a75e3479a6312b8990a163d1b7693254e))

Signed-off-by: Adria Montoto <75563346+adriamontoto@users.noreply.github.com>

- Improveintegermother tests reliability
  ([`cb7b433`](https://github.com/adriamontoto/object-mother-pattern/commit/cb7b433fee0e537d9796baacb5d9112f8c96b4cd))

- **dates**: Add missing tests for invalid_value methods
  ([`ee1281d`](https://github.com/adriamontoto/object-mother-pattern/commit/ee1281d990c70b149594b7b122c3c8cbadb59216))

Add test coverage for the invalid_value methods in StringDateMother and StringDatetimeMother
  classes. These tests verify that:

- The invalid_value method returns a string type - The returned value is not printable (contains
  non-printable characters)

This improves test coverage for the date-related mother classes and ensures proper validation of the
  invalid value generation functionality.

- **enumeration**: Implement enumeration mother tests
  ([`8c28dc6`](https://github.com/adriamontoto/object-mother-pattern/commit/8c28dc6aecb31e99a2941f057c09fc55512d00dc))

Signed-off-by: Adria Montoto <75563346+adriamontoto@users.noreply.github.com>

- **internet**: Add comprehensive tests for PortMother value object
  ([`5451d70`](https://github.com/adriamontoto/object-mother-pattern/commit/5451d709d21fb2a9eb790eb67bccdde6a53c87e1))

Adds unit tests for PortMother covering happy path, value, invalid type, standard port constants,
  and invalid_value edge cases. Ensures compatibility with IntegerMother and full coverage of public
  API.

- **internet**: Add unit tests for IPv4 and IPv6 address and network mothers
  ([`551a7a8`](https://github.com/adriamontoto/object-mother-pattern/commit/551a7a86e112c1036b771f099d13023b5c89935a))

Add comprehensive tests for IPv4AddressMother, IPv4NetworkMother, IPv6AddressMother, and
  IPv6NetworkMother in the internet domain, covering valid, invalid, and edge cases to ensure
  correct behavior and validation.

Signed-off-by: Adria Montoto <75563346+adriamontoto@users.noreply.github.com>

- **internet**: Implement mac address tests
  ([`e23d134`](https://github.com/adriamontoto/object-mother-pattern/commit/e23d134432585648ea0fcb2d0049b03c18c210e1))

Signed-off-by: Adria Montoto <75563346+adriamontoto@users.noreply.github.com>

- **money**: Implement BtcWalletMother tests
  ([`6e945fb`](https://github.com/adriamontoto/object-mother-pattern/commit/6e945fb1fa69461160dca8efcaad1693b78caecf))

- **people**: Implement fullname and username mothers tests
  ([`4aade0b`](https://github.com/adriamontoto/object-mother-pattern/commit/4aade0b2f0429da12c6303a41246d45cb7eaa375))

Signed-off-by: Adria Montoto <75563346+adriamontoto@users.noreply.github.com>

- **primitives**: Add complete test coverage for IntegerMother and FloatMother
  ([`47ddad0`](https://github.com/adriamontoto/object-mother-pattern/commit/47ddad07a4b61c4c211d55bf33d6fbfda6649c5b))

Add comprehensive test coverage for the out_of_range method in both IntegerMother and FloatMother
  classes. The new tests cover: - Happy path testing for out_of_range functionality - Type
  validation for min, max, and range parameters - Value validation for min/max relationship -
  Validation for negative range values

These tests ensure 100% code coverage for both classes and verify all edge cases and error
  conditions as specified in the method docstrings.
