
import pytest
import member_register


@pytest.fixture(autouse=True)
def reset_members():
    member_register.members.clear()


def test_register_member_success():
    result = member_register.register_member(
        "M001", "Alice", "alice@example.com", "9876543210"
    )
    assert result == "Member registered successfully!"


def test_register_member_missing_fields():
    result = member_register.register_member(
        "", "Alice", "alice@example.com", "9876543210"
    )
    assert result == "Error: All fields are required."


def test_register_member_duplicate_id():
    member_register.register_member(
        "M001", "Alice", "alice@example.com", "9876543210"
    )
    result = member_register.register_member(
        "M001", "Bob", "bob@example.com", "9876543211"
    )
    assert result == "Error: Member ID already exists."


def test_register_member_invalid_email():
    result = member_register.register_member(
        "M002", "Bob", "invalid-email", "9876543211"
    )
    assert result == "Error: Invalid email address."


def test_display_empty_members(capsys):
    member_register.display_members()
    captured = capsys.readouterr()
    assert "No members registered." in captured.out
