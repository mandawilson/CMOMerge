from pathlib import *

def getTumorType(projectPath):
	return projectPath.strip("/").split("/")[-4]

def getLabName(projectPath):
	return projectPath.strip("/").split("/")[-2]

def getInstitutionName(projectPath):
	return projectPath.strip("/").split("/")[-3]

def getProjectNumber(projectPath):
	return projectPath.strip("/").split("/")[-1]

def getStudyId(projectPath):
    print Path(projectPath) / "meta_study.txt"
