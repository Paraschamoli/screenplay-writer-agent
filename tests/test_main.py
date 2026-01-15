"""Tests for the Screenplay Writer Agent."""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from screenplay_writer_agent.main import handler


@pytest.mark.asyncio
async def test_handler_returns_response():
    """Test that handler accepts messages and returns a response."""
    messages = [{"role": "user", "content": "Write a screenplay about AI ethics"}]

    # Mock screenplay response (string, not MagicMock)
    mock_screenplay = "INT. LAB - DAY\n\nDR. ALEX works on an AI terminal..."

    with (
        patch("screenplay_writer_agent.main._initialized", True),
        patch("screenplay_writer_agent.main.run_crew", new_callable=AsyncMock, return_value=mock_screenplay),
    ):
        result = await handler(messages)

    # Verify we get a string (screenplay) back
    assert result is not None
    assert isinstance(result, str)
    assert "FADE IN" in result.upper() or "INT." in result.upper()


@pytest.mark.asyncio
async def test_handler_with_screenplay_query():
    """Test that handler processes screenplay writing queries correctly."""
    messages = [{"role": "user", "content": "Create a romantic comedy scene between two strangers"}]

    mock_screenplay = "EXT. PARK - DAY\n\nSARAH's dog runs toward MARK..."

    with (
        patch("screenplay_writer_agent.main._initialized", True),
        patch(
            "screenplay_writer_agent.main.run_crew", new_callable=AsyncMock, return_value=mock_screenplay
        ) as mock_run,
    ):
        result = await handler(messages)

    # Verify run_crew was called with the extracted input
    mock_run.assert_called_once_with("Create a romantic comedy scene between two strangers")
    assert result is not None
    assert isinstance(result, str)


@pytest.mark.asyncio
async def test_handler_initialization():
    """Test that handler initializes crew on first call."""
    messages = [{"role": "user", "content": "Write a short scene"}]

    mock_screenplay = "INT. ROOM - DAY\n\nCharacter speaks."

    # Start with _initialized as False to test initialization path
    with (
        patch("screenplay_writer_agent.main._initialized", False),
        patch("screenplay_writer_agent.main.initialize_crew", new_callable=AsyncMock) as mock_init,
        patch(
            "screenplay_writer_agent.main.run_crew", new_callable=AsyncMock, return_value=mock_screenplay
        ) as mock_run,
        patch("screenplay_writer_agent.main._init_lock", new_callable=MagicMock()) as mock_lock,
    ):
        # Configure the lock to work as an async context manager
        mock_lock_instance = MagicMock()
        mock_lock_instance.__aenter__ = AsyncMock(return_value=None)
        mock_lock_instance.__aexit__ = AsyncMock(return_value=None)
        mock_lock.return_value = mock_lock_instance

        result = await handler(messages)

        # Verify initialization was called
        mock_init.assert_called_once()
        # Verify run_crew was called
        mock_run.assert_called_once_with("Write a short scene")
        # Verify we got a result
        assert result is not None
        assert isinstance(result, str)


@pytest.mark.asyncio
async def test_handler_race_condition_prevention():
    """Test that handler prevents race conditions with initialization lock."""
    messages = [{"role": "user", "content": "Test screenplay query"}]

    mock_screenplay = "Test screenplay content"

    # Test with multiple concurrent calls
    with (
        patch("screenplay_writer_agent.main._initialized", False),
        patch("screenplay_writer_agent.main.initialize_crew", new_callable=AsyncMock) as mock_init,
        patch("screenplay_writer_agent.main.run_crew", new_callable=AsyncMock, return_value=mock_screenplay),
        patch("screenplay_writer_agent.main._init_lock", new_callable=MagicMock()) as mock_lock,
    ):
        # Configure the lock to work as an async context manager
        mock_lock_instance = MagicMock()
        mock_lock_instance.__aenter__ = AsyncMock(return_value=None)
        mock_lock_instance.__aexit__ = AsyncMock(return_value=None)
        mock_lock.return_value = mock_lock_instance

        # Call handler twice to ensure lock is used
        await handler(messages)
        await handler(messages)

        # Verify initialize_crew was called only once (due to lock)
        mock_init.assert_called_once()


@pytest.mark.asyncio
async def test_handler_with_character_development_query():
    """Test that handler can process character development queries."""
    messages = [{"role": "user", "content": "Develop a character for a cyberpunk detective story"}]

    mock_screenplay = "FADE IN:\n\nEXT. CITY - NIGHT\n\nDetective Raine investigates..."

    with (
        patch("screenplay_writer_agent.main._initialized", True),
        patch("screenplay_writer_agent.main.run_crew", new_callable=AsyncMock, return_value=mock_screenplay),
    ):
        result = await handler(messages)

    assert result is not None
    assert isinstance(result, str)
    assert "FADE IN" in result.upper()


@pytest.mark.asyncio
async def test_handler_empty_user_input():
    """Test that handler handles empty user input gracefully."""
    messages = [
        {"role": "system", "content": "You are a screenplay writer"},
        {"role": "assistant", "content": "How can I help you?"},
        # No user message
    ]

    with (
        patch("screenplay_writer_agent.main._initialized", True),
    ):
        result = await handler(messages)

    assert result is not None
    assert isinstance(result, str)
    assert "Please provide" in result


@pytest.mark.asyncio
async def test_handler_crew_exception():
    """Test that handler handles crew execution exceptions."""
    messages = [{"role": "user", "content": "Write a scene"}]

    with (
        patch("screenplay_writer_agent.main._initialized", True),
        patch("screenplay_writer_agent.main.run_crew", new_callable=AsyncMock) as mock_run,
    ):
        # Make run_crew raise an exception
        mock_run.side_effect = Exception("Crew execution failed")

        result = await handler(messages)

    assert result is not None
    assert isinstance(result, str)
    assert "FADE IN" in result.upper()
    assert "ERROR" in result.upper()


@pytest.mark.asyncio
async def test_handler_edge_case_malformed_messages():
    """Test handler with edge case malformed messages."""
    # Test with non-list input - handler returns error message instead of raising TypeError
    result = await handler("not a list")  # type: ignore[arg-type]
    assert result is not None
    assert isinstance(result, str)
    assert "ERROR" in result.upper()
    assert "Invalid input" in result

    # Test with empty list
    result = await handler([])
    assert result is not None
    assert isinstance(result, str)
    assert "Please provide" in result

    # Test with list but no user messages
    result = await handler([{"role": "system", "content": "test"}])
    assert result is not None
    assert isinstance(result, str)
    assert "Please provide" in result
