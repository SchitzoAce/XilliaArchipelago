from worlds.AutoWorld import AutoWorldRegister

def test_xillia_loaded():
    world_names = AutoWorldRegister.world_types.keys()
    assert "Xillia" in world_names, "Xillia world not registered"
    print("Xillia world is registered successfully!")

if __name__ == "__main__":
    test_xillia_loaded()
