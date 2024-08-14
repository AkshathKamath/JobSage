from openai import OpenAI
import os
# from dotenv import load_dotenv

# load_dotenv()

client = OpenAI(api_key = os.getenv('OPENAI_API_KEY'))

def summarize_resume(resume_text):
    summary_response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [
            {
                "role":"system",
                "content":"You are a helpful research assistant."
            },
            {
                "role":"user",
                "content":f"Summarize this resume: {resume_text} for a linkedin bio. Also add suitable roles interested in at the end of the summary. Remove any backslash-n as well from the summary.'"
            }
        ]
    )
    return summary_response.choices[0].message.content
    
    
# response = summarize_resume(resume_text)
# print(response)
# resume_text = """AKSHATHKAMATHKandivali(E),Mumbai400101,Indialakshathkamathwork@gmail.coml+919869468992\nEDUCATIONVelloreInstituteofTechnology,IndiaApril2023SecuredaBachelorofTechnologyinComputerScienceandEngineering.(CGPA:8.18/10)RelevantCourses:AppliedLinearAlgebra,StatisticsforEngineers,CalculusforEngineers,DiscreteMathematicsandGraphTheory,DataStructuresandAlgorithms,DataVisualization,MachineLearning.\nPROFESSIONALEXPERIENCEPwCIndia(PricewaterhouseCoopersInternationalLimited),Mumbai,IndiaJuly2023-PresentT e c h n o l o g yC o n s u l t a n t ,F i n a n c i a lS e r v i c e sT e c h n o l o g yT e a m\n●WorkingintheDevOpsteamforthedeploymentofaFinancialFraudandRiskManagement(FRM)solutioncalledBankIQforaclientbank.\n●CarriedoutcontainerizationfromDockerimagesoftheFRMmoduleandmanagementofthecontainersusingKubernetes.\n●LeveragingAWSservicessuchasEKSformanagingcontainersremotelyonthecloudinanEC2environmentandAmazonS3forstorage.\nT e c h n o l o g yC o n s u l t a n tI n t e r n ,F i n a n c i a lS e r v i c e sT e c h n o l o g yT e a mJanuary2023-July2023\n●CollaboratedwiththeBackendteamontheUnifiedPaymentsInterfaceReconciliationprojectwithGoogleandNPCIasclients.\n●UtilizedPostgreSQLasthedatabasetostoretransactionsfromtheissuer,acquirerbanks,andmediary(NPCI),andusedSQLtomatchtransactionsbasedoncertaincriteriatocategorizethemassuccessful.\n●TaskedwithdevelopingawebappusingDjangotoviewtheReconciliationmodule,andusedPythontofetchtransactionsfromthedatabaseandprovidethemtothefrontendteam.\nSurplus,Mumbai,IndiaJuly2022-October2022D a t aA n a l y s i sI n t e r nSurplusisapersonalfinancemanagementappthatauto-tracksexpenses,andtailorsrecommendationstohelpusersmakesmartertransactions.\n●FetcheduserexpensedatafromAmazonS3storageusingPython,andcreateddashboardsusingSeabornandPlotlylibrariessouserscouldviewtheirexpensesinvariouscategoriesinvarioustimeframes.\n●Analyzedexpensedataforeachuser,usingPython,bycalculatingparametersofExpensefrequency,distribution,Averagetimebetweenexpensesofsimilarcategories,etc.;categorizedtheusersfurther,basedonthecalculatedmetrics.\n●Assistedtheengineeringteamincreatingarecommendationmodel,tosuggestuserstohandleexpensesandmaximizesavings.\n●AssignedtoworkonthedeploymentofthecreatedMLmodelsintothecloudusingAWSSageMaker\nDvimayTechnologies,Mumbai,IndiaJune2021-July2021F r o n t e n dD e v e l o p e rI n t e r nDvimayTechnologiesisaservice-basedcompanyprovidingITsolutionstoitsclients.\n●Redesignedthecompany’spublicwebsiteusingHTML,CSS,andJavaScript,workingwithUIandfrontendwebteam.\n●ImplementedFigmafordesignandReact.jstodevelopthewebsitebasedonrequirementsandcustomerfeedback.\nACADEMICPROJECTSANDPAPERSAutomatedKneeInjuryDiagnosisusingDeepLearning\n●EmployedtheMRNetDataconsistingofMRIscansofthekneeandappliedpreprocessing,andaugmentationstepstothedatasettoprepareitforthemodel.\n●BuiltaCNNmodeltocategorizetheMRIscansbasedontheinjuryandcomparedtheresultswithpre-trainedAlexNetandSqueezeNetmodels.Improvedaccuracyofthemodelusingtheensemblingtechnique ●Authoredandpublishedaresearchpaperonthesameinthei-manager’sJournalonComputerScience(JCOM:VolumeNo.11,IssueNo.2,July-September2023)ISSN:2347-6141.\nSmartDustbinforRecyclableWasteSegregation\n●Createdasmartdustbintoidentifyandseparaterecyclablewastefromorganicwaste.\n●TrainedaCNNmodelusingDeepLearningtocategorizewasteintorecyclablesfromalivecamerafeed.\n●ProgrammedArduinoUnoboardusingC++,tocontrolthelidoftherespectivedustbinbasedonthemodel’soutput.\n●ParticipatedinandintotheSemi-FinalroundofCodeFury6.0hackathonbyUniversityVisvesvarayaCollegeofEngineering(UVCE)in2023."""