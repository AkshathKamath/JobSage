from openai import OpenAI
import os
# from dotenv import load_dotenv

# load_dotenv()

client = OpenAI(api_key = os.getenv('OPENAI_API_KEY'))

def compare_resume(resume_text, job_description, role):
    summary_response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [
            {
                "role":"system",
                "content":"You are a helpful research assistant."
            },
            {
                "role":"user",
                "content":f"Suggest improvements on this resume: {resume_text} to better fit this job description: {job_description} for the role: {role}. Kepp the improvements technical in nature. Just provide the improvements nothing more. Provide them as a numbered list without any headings."
            }
        ]
    )
    return summary_response.choices[0].message.content

# resume_text = """AKSHATHKAMATHKandivali(E),Mumbai400101,Indialakshathkamathwork@gmail.coml+919869468992\nEDUCATIONVelloreInstituteofTechnology,IndiaApril2023SecuredaBachelorofTechnologyinComputerScienceandEngineering.(CGPA:8.18/10)RelevantCourses:AppliedLinearAlgebra,StatisticsforEngineers,CalculusforEngineers,DiscreteMathematicsandGraphTheory,DataStructuresandAlgorithms,DataVisualization,MachineLearning.\nPROFESSIONALEXPERIENCEPwCIndia(PricewaterhouseCoopersInternationalLimited),Mumbai,IndiaJuly2023-PresentT e c h n o l o g yC o n s u l t a n t ,F i n a n c i a lS e r v i c e sT e c h n o l o g yT e a m\n●WorkingintheDevOpsteamforthedeploymentofaFinancialFraudandRiskManagement(FRM)solutioncalledBankIQforaclientbank.\n●CarriedoutcontainerizationfromDockerimagesoftheFRMmoduleandmanagementofthecontainersusingKubernetes.\n●LeveragingAWSservicessuchasEKSformanagingcontainersremotelyonthecloudinanEC2environmentandAmazonS3forstorage.\nT e c h n o l o g yC o n s u l t a n tI n t e r n ,F i n a n c i a lS e r v i c e sT e c h n o l o g yT e a mJanuary2023-July2023\n●CollaboratedwiththeBackendteamontheUnifiedPaymentsInterfaceReconciliationprojectwithGoogleandNPCIasclients.\n●UtilizedPostgreSQLasthedatabasetostoretransactionsfromtheissuer,acquirerbanks,andmediary(NPCI),andusedSQLtomatchtransactionsbasedoncertaincriteriatocategorizethemassuccessful.\n●TaskedwithdevelopingawebappusingDjangotoviewtheReconciliationmodule,andusedPythontofetchtransactionsfromthedatabaseandprovidethemtothefrontendteam.\nSurplus,Mumbai,IndiaJuly2022-October2022D a t aA n a l y s i sI n t e r nSurplusisapersonalfinancemanagementappthatauto-tracksexpenses,andtailorsrecommendationstohelpusersmakesmartertransactions.\n●FetcheduserexpensedatafromAmazonS3storageusingPython,andcreateddashboardsusingSeabornandPlotlylibrariessouserscouldviewtheirexpensesinvariouscategoriesinvarioustimeframes.\n●Analyzedexpensedataforeachuser,usingPython,bycalculatingparametersofExpensefrequency,distribution,Averagetimebetweenexpensesofsimilarcategories,etc.;categorizedtheusersfurther,basedonthecalculatedmetrics.\n●Assistedtheengineeringteamincreatingarecommendationmodel,tosuggestuserstohandleexpensesandmaximizesavings.\n●AssignedtoworkonthedeploymentofthecreatedMLmodelsintothecloudusingAWSSageMaker\nDvimayTechnologies,Mumbai,IndiaJune2021-July2021F r o n t e n dD e v e l o p e rI n t e r nDvimayTechnologiesisaservice-basedcompanyprovidingITsolutionstoitsclients.\n●Redesignedthecompany’spublicwebsiteusingHTML,CSS,andJavaScript,workingwithUIandfrontendwebteam.\n●ImplementedFigmafordesignandReact.jstodevelopthewebsitebasedonrequirementsandcustomerfeedback.\nACADEMICPROJECTSANDPAPERSAutomatedKneeInjuryDiagnosisusingDeepLearning\n●EmployedtheMRNetDataconsistingofMRIscansofthekneeandappliedpreprocessing,andaugmentationstepstothedatasettoprepareitforthemodel.\n●BuiltaCNNmodeltocategorizetheMRIscansbasedontheinjuryandcomparedtheresultswithpre-trainedAlexNetandSqueezeNetmodels.Improvedaccuracyofthemodelusingtheensemblingtechnique ●Authoredandpublishedaresearchpaperonthesameinthei-manager’sJournalonComputerScience(JCOM:VolumeNo.11,IssueNo.2,July-September2023)ISSN:2347-6141.\nSmartDustbinforRecyclableWasteSegregation\n●Createdasmartdustbintoidentifyandseparaterecyclablewastefromorganicwaste.\n●TrainedaCNNmodelusingDeepLearningtocategorizewasteintorecyclablesfromalivecamerafeed.\n●ProgrammedArduinoUnoboardusingC++,tocontrolthelidoftherespectivedustbinbasedonthemodel’soutput.\n●ParticipatedinandintotheSemi-FinalroundofCodeFury6.0hackathonbyUniversityVisvesvarayaCollegeofEngineering(UVCE)in2023."""

# job_description = """1- 3+ years experience building and developing backend applications
# Bachelor's or Master's degree with a preference for Computer Science degree
# Experience crafting and implementing highly scalable and performant RESTful micro-services
# Proficiency in any modern object-oriented programming language (e.g., Java, Kotlin, Go, Scala, Python, etc.)
# Fluency in any one database technology (e.g. RDBMS like Oracle or Postgres and/or NoSQL like DynamoDB or Cassandra)
# Real passion for collaboration and strong interpersonal and communication skills
# Broad knowledge and understanding of SaaS, PaaS, IaaS industry with hands-on experience of public cloud offerings (AWS, GAE, Azure)
# Familiarity with cloud architecture patterns and an engineering discipline to produce software with quality
# """

# print(compare_resume(resume_text, job_description, "Backend Engineer"))