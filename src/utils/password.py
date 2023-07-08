from zxcvbn import zxcvbn


def checkStrength(userPass):
    """Gives Password strength and suggestion to improve the password

    Args:
        password (str): password entered by the user

    Returns:
        dict: {"strength": int, "suggestion": str}
    """

    result = zxcvbn(password=userPass, user_inputs=[])
    return {"strength": result["score"], "suggestion": result["feedback"]["suggestions"]}
