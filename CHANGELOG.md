# CHANGELOG

<!-- version list -->

## v3.7.0 (2025-12-08)

### ✨ Features

- Support python 3.14
  ([`dc02a53`](https://github.com/adriamontoto/object-mother-pattern/commit/dc02a53f4755e5a1fa036dd284e81fd2a4ce10c0))


## v3.6.0 (2025-09-10)

### ✨ Features

- Implement exclude parameter to create method in EnumerationMother for filtering values
  ([`6b001d4`](https://github.com/adriamontoto/object-mother-pattern/commit/6b001d440f7616bd98b58b351f11f9bc999f599a))


## v3.5.1 (2025-08-26)

### 🐛 Bug Fixes

- Rename allow_versions to exclude_versions in UUID mothers
  ([`7833c8c`](https://github.com/adriamontoto/object-mother-pattern/commit/7833c8c6404facfa5022c5256ce924c900dd68f2))


## v3.5.0 (2025-08-26)

### ✨ Features

- Implement v1, v3, v5 uuid mothers and string representations
  ([`036ce5e`](https://github.com/adriamontoto/object-mother-pattern/commit/036ce5e699c0f23befe5f720d486a5c5056e0756))


## v3.4.1 (2025-08-26)

### 🐛 Bug Fixes

- Ensure generated user agent has no trailing spaces
  ([`1133db7`](https://github.com/adriamontoto/object-mother-pattern/commit/1133db75ff3cb1a96e603d5ebb946606f9493787))


## v3.4.0 (2025-08-26)

### ✨ Features

- **internet**: Implement ip address mother
  ([`a04512a`](https://github.com/adriamontoto/object-mother-pattern/commit/a04512a1afabe733a03348a6d2a8ad4b91be08d3))

- **internet**: Implement user agent mother
  ([`db4b267`](https://github.com/adriamontoto/object-mother-pattern/commit/db4b26790eec24a1b239c053cd01f5024c680312))


## v3.3.1 (2025-08-25)

### 🐛 Bug Fixes

- Ensure mother_type is a class before checking for ValueObject subclass
  ([`a7bd44e`](https://github.com/adriamontoto/object-mother-pattern/commit/a7bd44eac23eec9b81491b7496ffbcedf853b3e1))


## v3.3.0 (2025-08-25)

### ✨ Features

- Implement RFC-compliant domain generation
  ([`9d17348`](https://github.com/adriamontoto/object-mother-pattern/commit/9d17348182e3afd0eaea2c0c081eb55b5d17bffe))

- Integrate value-object library for obtaining value object primitive type
  ([`79292c9`](https://github.com/adriamontoto/object-mother-pattern/commit/79292c9a9e7b589d3d65fb433a806f633afc1a84))


## v3.2.0 (2025-08-03)

### ✨ Features

- Implement UUID v4 and String UUID v4 mothers
  ([`7768bad`](https://github.com/adriamontoto/object-mother-pattern/commit/7768badd7f494a4c2e1d1fea9be78ddcddf71d52))


## v3.1.1 (2025-06-30)

### 🐛 Bug Fixes

- Accept GenericAliases as BaseMother type
  ([`0d429fa`](https://github.com/adriamontoto/object-mother-pattern/commit/0d429fa6e64e458906ed6fb4f391b1131c54795c))


## v3.1.0 (2025-06-28)

### ✨ Features

- Implement length in StringMother.invalid_value
  ([`786b202`](https://github.com/adriamontoto/object-mother-pattern/commit/786b202f5bc6be0ba8c36307a955088d685c0626))

- Override FloatMother invalid type to remove integer as well
  ([`515da32`](https://github.com/adriamontoto/object-mother-pattern/commit/515da321d72324dfbc73454105a8180c1c97650c))


## v3.0.0 (2025-06-21)

### ✨ Features

- Move models folder and its imports
  ([`d5e7140`](https://github.com/adriamontoto/object-mother-pattern/commit/d5e71408918cb07c12fa557b71d878a3e03832ef))


## v2.1.1 (2025-06-21)

### 🐛 Bug Fixes

- Improve base mother create method type
  ([`d3cbcf3`](https://github.com/adriamontoto/object-mother-pattern/commit/d3cbcf34cd699b9f521cc2a221094cf74f76237c))


## v2.1.0 (2025-06-21)

### 🐛 Bug Fixes

- Add noqa statement to discard warnings
  ([`7a525c0`](https://github.com/adriamontoto/object-mother-pattern/commit/7a525c0dc6ec513edfd81e0b7e57954ba3fae1e0))

### ✨ Features

- Implement timezone object mother
  ([`0794635`](https://github.com/adriamontoto/object-mother-pattern/commit/07946352cd01d471137685e0b78470ae92739965))


## v2.0.0 (2025-06-16)

### 📦 Build System

- Remove pyproject extra space
  ([`7333621`](https://github.com/adriamontoto/object-mother-pattern/commit/7333621e659023409608a59be604dadf900e452c))

### ✨ Features

- Rework how enumeration works, now you have to create a new class of type Enum
  ([`49dd756`](https://github.com/adriamontoto/object-mother-pattern/commit/49dd75634db4b0480c1563679f239d7eff3e7150))


## v1.1.0 (2025-06-16)

### ✨ Features

- Remove type attribute from child mothers
  ([`6c97765`](https://github.com/adriamontoto/object-mother-pattern/commit/6c97765bf3b4d7dc41337e5dc89b90d73bd92d58))


## v1.0.0 (2025-06-09)

### ✨ Features

- Unify cases between mothers ([#56](https://github.com/adriamontoto/object-mother-pattern/pull/56),
  [`f5b58ff`](https://github.com/adriamontoto/object-mother-pattern/commit/f5b58ff0fe311907eeba7909b061509ed2e8bc76))


## v0.4.1 (2025-06-09)

### 🐛 Bug Fixes

- Remove those vales that has length 0
  ([`799c488`](https://github.com/adriamontoto/object-mother-pattern/commit/799c4889dec2db930b91a57ab0f5dffeea84bd18))


## v0.4.0 (2025-06-09)

### ✨ Features

- **internet**: Implement domain mother
  ([#55](https://github.com/adriamontoto/object-mother-pattern/pull/55),
  [`dc8145e`](https://github.com/adriamontoto/object-mother-pattern/commit/dc8145eafaead747edcfa1f9186acb687f9cc48e))


## v0.3.3 (2025-06-08)

### 📦 Build System

- Remove tests from the build process
  ([`57aa91a`](https://github.com/adriamontoto/object-mother-pattern/commit/57aa91a059f90245223c24b6395a19693132e807))


## v0.3.2 (2025-06-08)

### 📦 Build System

- Use uv tool to create venv and install dependencies
  ([`e87e725`](https://github.com/adriamontoto/object-mother-pattern/commit/e87e725b2dceacb1fd2fe07ae02117c9d53fc1b9))


## v0.3.1 (2025-06-08)

### 📦 Build System

- Remove requirements files to only use pyproject
  ([`fc4f877`](https://github.com/adriamontoto/object-mother-pattern/commit/fc4f877f12f5526ed65f88715d701db0eae88bf9))


## v0.3.0 (2025-06-07)

### ✨ Features

- Implement text mother ([#52](https://github.com/adriamontoto/object-mother-pattern/pull/52),
  [`9ddf1f4`](https://github.com/adriamontoto/object-mother-pattern/commit/9ddf1f48150c97dedc4af2c6b2da4d2863f88f07))


## v0.2.0 (2025-06-07)

### 🐛 Bug Fixes

- Remove build when creating a new version
  ([`8e3a17b`](https://github.com/adriamontoto/object-mother-pattern/commit/8e3a17bdeaf3b8c4c9fccae92fafeaa338fc8a7d))

- Remove nextafter function and inf
  ([`24a4f52`](https://github.com/adriamontoto/object-mother-pattern/commit/24a4f52103296a6a0132d7a9b340a139100deaf7))

### ✨ Features

- Implement adjustable probability of true boolean creation
  ([#49](https://github.com/adriamontoto/object-mother-pattern/pull/49),
  [`04e54a0`](https://github.com/adriamontoto/object-mother-pattern/commit/04e54a0091a0eb930709a2d190614c74ee6f3d96))


## v0.1.1 (2025-05-25)

### 🐛 Bug Fixes

- Update password tests to create correct passwords
  ([`b2548b7`](https://github.com/adriamontoto/object-mother-pattern/commit/b2548b72000bfbba674eab06e0c12b7f112e098e))


## v0.1.0 (2025-05-25)

### 🐛 Bug Fixes

- Add coverage pragma comments for edge case handling in NameMother and TextMother
  ([`2fa0d81`](https://github.com/adriamontoto/object-mother-pattern/commit/2fa0d8115ea6a7ca0fe2942db3fb774365e766a9))

- Add coverage pragma comments for list, set, tuple, dict, and datetime types in BaseMother class
  ([`1a981df`](https://github.com/adriamontoto/object-mother-pattern/commit/1a981df1746c5b71bd5f62f88254a2b0b81e629a))

- Add coverage pragma comments in DatetimeMother and NameMother for clarity
  ([`13987bd`](https://github.com/adriamontoto/object-mother-pattern/commit/13987bda5528189424218501b17ae8c254083589))

- Fix lint and coverage returning errors
  ([`a7b14e6`](https://github.com/adriamontoto/object-mother-pattern/commit/a7b14e6bd100fe5c2f38f4fdb52e0cbfd16ee532))

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

- **tests**: Ensure positive min_length in PasswordMother random_length tests
  ([`c7a5336`](https://github.com/adriamontoto/object-mother-pattern/commit/c7a5336c9207491a49ea55e2d90246332e5bab11))

### 📦 Build System

- Add new dependencies to the package
  ([`9a69232`](https://github.com/adriamontoto/object-mother-pattern/commit/9a692320a9f2bdc2f174a31e86ad7088a26e432f))

- Create version 2024.12.21
  ([`9d6c326`](https://github.com/adriamontoto/object-mother-pattern/commit/9d6c32630a0bae1ed4733a45c8358daf7ac761d4))

- Make package versions more permissible
  ([`d97a13f`](https://github.com/adriamontoto/object-mother-pattern/commit/d97a13f7105a4b61c41cb35e27baa304df32c328))

- Remove linting error when removing noqa comments
  ([`0bbb523`](https://github.com/adriamontoto/object-mother-pattern/commit/0bbb523cd00461ac9009db572d01fc0c7f3cbcd3))

- Remove pytest-asyncio from development requirements
  ([`510c093`](https://github.com/adriamontoto/object-mother-pattern/commit/510c09357739c6148b27b11fbdb70ab78e9d600a))

- Simplify .gitignore file
  ([`bf8800f`](https://github.com/adriamontoto/object-mother-pattern/commit/bf8800fbc95bca0e5b082a45328b87591b74d800))

- Simplify .gitignore file
  ([`7205927`](https://github.com/adriamontoto/object-mother-pattern/commit/72059274ae32d4eb2b02ab36d7085390580772f6))

- Update .gitignore to exclude all coverage files
  ([`b0af1a1`](https://github.com/adriamontoto/object-mother-pattern/commit/b0af1a16cea1954c5959fc5ad65dbb55af72f829))

- Update .gitignore to exclude coverage and environment folders
  ([`ed21e12`](https://github.com/adriamontoto/object-mother-pattern/commit/ed21e1204e33c5637cf43457c3fb08f48c30f7ff))

- Update faker requirement
  ([`0ca9ee3`](https://github.com/adriamontoto/object-mother-pattern/commit/0ca9ee3277d872bcdfdb1d2dc569867d4afb6182))

### ✨ Features

- Add BoolMother class for generating random boolean values
  ([`e5fae0e`](https://github.com/adriamontoto/object-mother-pattern/commit/e5fae0eae347953e9e30853728ba3a5deb1f2c06))

- Add echos to print the status of the command in makefile
  ([`05c2363`](https://github.com/adriamontoto/object-mother-pattern/commit/05c23638f2f82bb0a65d358cd97f586c96de793b))

- Add IntegerMother class for generating random integers
  ([`dabe2fc`](https://github.com/adriamontoto/object-mother-pattern/commit/dabe2fc8272dfc5cfccbf0a22e5d31ddb8b01fbe))

- Add invalid_value method to StringDateMother and StringDatetimeMother classes
  ([`b11b645`](https://github.com/adriamontoto/object-mother-pattern/commit/b11b645d4133903bb4abee541077cc4b017ddc8c))

- Add TLD domains list
  ([`b0713b2`](https://github.com/adriamontoto/object-mother-pattern/commit/b0713b209bc4e7b6f93c378480cfa4c4b3677197))

- Create alias for install dev dependencies and execute tests
  ([`ec2f9d1`](https://github.com/adriamontoto/object-mother-pattern/commit/ec2f9d1d1f476c6fa677da4e63f7f307f3410339))

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

- Simplify float mother api
  ([`a6b0d15`](https://github.com/adriamontoto/object-mother-pattern/commit/a6b0d15ccfdfb33a571a497f6ebf3ffa39d1203a))

- Simplify string mother api
  ([`69229ba`](https://github.com/adriamontoto/object-mother-pattern/commit/69229ba2015cd2c60f102a10527b95bfc5ffdd76))

- Update FloatMother to allow random decimal places when not specified
  ([`c0aff1b`](https://github.com/adriamontoto/object-mother-pattern/commit/c0aff1bcf20d33456622ac7273a6ac2bd1a41075))

- **aws regions**: Add invalid_value method to AwsCloudRegionMother and tests
  ([`8d49b96`](https://github.com/adriamontoto/object-mother-pattern/commit/8d49b969441a9ac8daccdf3dbf95d1550494f642))

- **identifiers**: Add Spanish DNI Mother implementation
  ([`23a8d58`](https://github.com/adriamontoto/object-mother-pattern/commit/23a8d58895c9db4f0140fef5d58ed9b56493e539))

- **identifiers**: Implement nie mother
  ([`511c954`](https://github.com/adriamontoto/object-mother-pattern/commit/511c954ebb301d13c6060586711a433fd0bd3b00))

- **people**: Implement password mother
  ([`ea9c711`](https://github.com/adriamontoto/object-mother-pattern/commit/ea9c711291ecf6c8d41c4fa16b7371af6a8144ae))

### 🚀 Performance Improvements

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
