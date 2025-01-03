"""
BytesMother module.
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

from object_mother_pattern.mothers.base_mother import BaseMother


class BytesMother(BaseMother[bytes]):
    """
    BytesMother class.

    Example:
    ```python
    from object_mother_pattern.mothers import BytesMother

    bytes = BytesMother.create()
    print(bytes)
    # >>> 'zFUmlsODZqzwyGjrOOqBtYzNwlJdOETalkXbuSegoQpgEnYQTCDeoifWrTQXMm'
    ```
    """

    _type: type = bytes

    @classmethod
    @override
    def create(cls, *, value: bytes | None = None, min_length: int = 1, max_length: int = 128) -> bytes:
        """
        Create a random bytes value.

        Args:
            value (bytes | None, optional): Bytes value. Defaults to None.

        Raises:
            TypeError: If value is not bytes.
            TypeError: If min_length is not an integer.
            TypeError: If max_length is not an integer.
            ValueError: If min_length is less than 1.
            ValueError: If max_length is less than 1.
            ValueError: If min_length is greater than max_length.

        Returns:
            bytes: Random bytes.

        Example:
        ```python
        from object_mother_pattern.mothers import BytesMother

        bytes = BytesMother.create()
        print(bytes)
        # >>> b'zFUmlsODZqzwyGjrOOqBtYzNwlJdOETalkXbuSegoQpgEnYQTCDeoifWrTQXMm'
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

        if min_length < 1:
            raise ValueError('BytesMother min_length must be greater than 0.')

        if max_length < 1:
            raise ValueError('BytesMother max_length must be greater than 0.')

        if min_length > max_length:
            raise ValueError('BytesMother min_length must be less than or equal to max_length.')

        return cls._random().pystr(min_chars=min_length, max_chars=max_length).encode()

    @classmethod
    def of_length(cls, *, length: int) -> bytes:
        """
        Create a bytes of a specific length.

        Args:
            length (int): Length of the bytes.

        Raises:
            TypeError: If length is not a bytes.
            ValueError: If length is less than 1.

        Returns:
            bytes: Bytes of a specific length.

        Example:
        ```python
        from object_mother_pattern.mothers import BytesMother

        bytes = BytesMother.of_length(length=10)
        print(bytes)
        # >>> b'TfkrYRxUFT'
        ```
        """
        return cls.create(min_length=length, max_length=length)
