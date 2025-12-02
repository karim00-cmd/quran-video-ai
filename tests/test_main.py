import app.main as main_module

def test_main_returns_ok():
    assert main_module.main() == "quran-video-ai: OK"