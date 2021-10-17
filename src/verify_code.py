class VerifyCode():
    """
    Verify the code send by an user to check with the DB
    and return OK or not
    """

    def __init__(self, code:str) -> None:
        self.code = code
    
    def check_code(self) -> bool:
        """
        Check if the code is correct
        """
        if self.code == "1234":
            return True
        return False
    