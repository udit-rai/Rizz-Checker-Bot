import base64
import pytest
from pathlib import Path
from rizz import load_image_b64, build_image_blocks, build_system_prompt

#Temporary png to test
@pytest.fixture
def temp_png(tmp_path):
    # tiny 1x1 PNG
    png_data = base64.b64decode(
        "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/wIAAgMBApGN38sAAAAASUVORK5CYII="
    )
    file_path = tmp_path / "test.png"
    file_path.write_bytes(png_data)
    return str(file_path)

# Temporary png
def test_load_image_b64(temp_png):
    mime, b64 = load_image_b64(temp_png)
    assert mime == "image/png"
    assert isinstance(b64, str)
    assert len(b64) > 10  

# Temporary png
def test_build_image_blocks(temp_png):
    blocks = build_image_blocks([temp_png])
    assert isinstance(blocks, list)
    assert len(blocks) == 1
    block = blocks[0]
    assert block["type"] == "input_image"
    assert block["image_url"].startswith("data:image/png;base64,")


def test_build_system_prompt():
    prompt = build_system_prompt()
    assert isinstance(prompt, str)
    # assert "AI assistant specialized in analyzing group chat dynamics" in prompt
    assert len(prompt) > 50
