def verifyStance(rightShoulderAngle, leftShoulderAngle, rightHipAngle, leftHipAngle):
    if 100 > rightShoulderAngle > 90 and 70 > leftShoulderAngle > 60 and 100 > rightHipAngle > 90 and 90 > leftHipAngle > 80:
        return True
    if 100 > leftShoulderAngle > 90 and 70 > rightShoulderAngle > 60 and 100 > leftHipAngle > 90 and 90 > rightHipAngle > 80:
        return True
    return False
