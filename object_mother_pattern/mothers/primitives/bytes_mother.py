"""
BytesMother module.
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

from random import randbytes, randint

from object_mother_pattern.models import BaseMother


class BytesMother(BaseMother[bytes]):
    r"""
    BytesMother class is responsible for creating random bytes values.

    Example:
    ```python
    from object_mother_pattern import BytesMother

    bytes = BytesMother.create()
    print(bytes)
    # >>> b'xN\xd9\xb7\xc7\x8bO\x81\x14\xd7\xcdiE'
    ```
    """

    @classmethod
    @override
    def create(cls, *, value: bytes | None = None, min_length: int = 1, max_length: int = 128) -> bytes:
        r"""
        Create a random bytes value. If a specific bytes value is provided via `value`, it is returned after validation.
        Otherwise, a random bytes value is generated with a length randomly chosen between `min_length` and
        `max_length` (both included).

        Args:
            value (bytes | None, optional): A specific bytes value to return. Defaults to None.
            min_length (int, optional): Minimum length of the generated bytes. Must be >= 0. Defaults to 1.
            max_length (int, optional): Maximum length of the generated bytes. Must be >= `min_length`. Defaults to 128.

        Raises:
            TypeError: If the provided `value` is not of type bytes.
            TypeError: If `min_length` is not an integer.
            TypeError: If `max_length` is not an integer.
            ValueError: If `min_length` is less than 0.
            ValueError: If `max_length` is less than 0.
            ValueError: If `min_length` is greater than `max_length`.

        Returns:
            bytes: A randomly generated bytes value.

        Example:
        ```python
        from object_mother_pattern import BytesMother

        bytes = BytesMother.create()
        print(bytes)
        # >>> b'xN\xd9\xb7\xc7\x8bO\x81\x14\xd7\xcdiE'
        ```
        """
        if value is not None:
            if type(value) is not bytes:
                raise TypeError('BytesMother value must be bytes.')

            return value

        if type(min_length) is not int:
            raise TypeError('BytesMother min_length must be an integer.')

        if type(max_length) is not int:
            raise TypeError('BytesMother max_length must be an integer.')

        if min_length < 0:
            raise ValueError('BytesMother min_length must be greater than or equal to 0.')

        if max_length < 0:
            raise ValueError('BytesMother max_length must be greater than or equal to 0.')

        if min_length > max_length:
            raise ValueError('BytesMother min_length must be less than or equal to max_length.')

        length = randint(a=min_length, b=max_length)  # noqa: S311
        return randbytes(n=length)  # noqa: S311

    @classmethod
    def empty(cls) -> bytes:
        """
        Create an empty bytes value.

        Returns:
            bytes: Empty bytes.

        Example:
        ```python
        from object_mother_pattern import BytesMother

        bytes = BytesMother.empty()
        print(bytes)
        # >>> b''
        ```
        """
        return b''

    @classmethod
    def of_length(cls, *, length: int) -> bytes:
        r"""
        Create a bytes value of a specific length.

        Args:
            length (int): The length of the bytes value to generate. Must be >= 1.

        Raises:
            TypeError: If `length` is not an integer.
            ValueError: If `length` is less than 1.

        Returns:
            bytes: A randomly generated bytes value of the specified `length`.

        Example:
        ```python
        from object_mother_pattern import BytesMother

        bytes = BytesMother.of_length(length=10)
        print(bytes)
        # >>> b'\xbeyh\x88d\xd2\xe5\xb6\xa5\x89'
        ```
        """
        if type(length) is not int:
            raise TypeError('BytesMother length must be an integer.')

        if length < 1:
            raise ValueError('BytesMother length must be greater than or equal to 1.')

        return cls.create(min_length=length, max_length=length)
