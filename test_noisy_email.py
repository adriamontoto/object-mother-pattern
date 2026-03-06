# #!/usr/bin/env python3
# """Test script for _noisy_email_address implementation."""

# from object_mother_pattern.mothers.internet import EmailAddressMother

# def test_noisy_email_address():
#     """Test the _noisy_email_address method with various inputs."""
    
#     # Test with no noise
#     result = EmailAddressMother._noisy_email_address(
#         local_part="testuser",
#         include_special_chars=False,
#         include_numbers=False
#     )
#     print(f"No noise: {result}")
#     assert result == "testuser", "Should return unchanged when no noise requested"
    
#     # Test with numbers only
#     for i in range(5):
#         result = EmailAddressMother._noisy_email_address(
#             local_part="testuser",
#             include_special_chars=False,
#             include_numbers=True
#         )
#         print(f"Numbers only (attempt {i+1}): {result}")
#         # Check that numbers were added
#         has_numbers = any(c.isdigit() for c in result)
#         assert has_numbers, "Should contain at least one number"
#         assert "testuser" in result or any(c in result for c in "testuser"), "Should contain original characters"
    
#     # Test with special chars only
#     for i in range(5):
#         result = EmailAddressMother._noisy_email_address(
#             local_part="testuser",
#             include_special_chars=True,
#             include_numbers=False
#         )
#         print(f"Special chars only (attempt {i+1}): {result}")
#         # Check for special characters
#         special_chars = ['.', '_', '-', '+']
#         has_special = any(c in result for c in special_chars)
#         assert has_special or result == "testuser", "Should contain special char or be unchanged"
#         # Check RFC compliance
#         assert not result.startswith('.'), "Should not start with dot"
#         assert not result.endswith('.'), "Should not end with dot"
#         assert '..' not in result, "Should not have consecutive dots"
    
#     # Test with both numbers and special chars
#     for i in range(5):
#         result = EmailAddressMother._noisy_email_address(
#             local_part="testuser",
#             include_special_chars=True,
#             include_numbers=True
#         )
#         print(f"Both noise types (attempt {i+1}): {result}")
#         # Verify it's not empty
#         assert result, "Result should not be empty"
#         # Check RFC compliance
#         assert not result.startswith('.'), "Should not start with dot"
#         assert not result.endswith('.'), "Should not end with dot"
#         assert '..' not in result, "Should not have consecutive dots"
    
#     # Test with short input
#     result = EmailAddressMother._noisy_email_address(
#         local_part="a",
#         include_special_chars=True,
#         include_numbers=True
#     )
#     print(f"Short input with noise: {result}")
#     assert result, "Should handle short input"
    
#     # Test with empty string edge case
#     result = EmailAddressMother._noisy_email_address(
#         local_part="",
#         include_special_chars=True,
#         include_numbers=True
#     )
#     print(f"Empty input: {result}")
#     assert result == "", "Should handle empty input gracefully"
    
#     print("\nAll tests passed!")

# if __name__ == "__main__":
#     test_noisy_email_address()