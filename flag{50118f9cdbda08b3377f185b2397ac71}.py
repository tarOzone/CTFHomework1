from app import app, ans_dict


if __name__ == "__main__":
    try:
        app.run('0.0.0.0', 5000, debug=False)
    except KeyboardInterrupt:
        pass
    finally:
        ans_dict.close()
