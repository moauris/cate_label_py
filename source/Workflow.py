
class Workflow:
    def __init__(self, inputDir, outputDir = ""):
        if(len(outputDir) == 0):
            outputDir = inputDir + "_output.xlsx"
        self.InputDir = inputDir
        self.outputDir = outputDir

    
