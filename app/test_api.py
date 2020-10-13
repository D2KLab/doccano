from api.models import SequenceLabelingProject, Project, Document, Label, SequenceAnnotation, RoleMapping, Role
from api.utils import SequenceLabelingStorage
from django.contrib.auth.models import User

datas = {"text": "WHO DOES SPAIN OFFER INTERNATIONAL PROTECTION TO? - To refugees, namely those with a well-founded fear of being persecuted in their country for reasons of race, religion, nationality, political opinions, belonging to a particular social group, gender or sexual orientation\nRefugees are granted the right to asylum\n- Foreigners who are not refugees but who do not wish to return to their native country for reasons which imply a genuine risk of suffering any of the following: - Death sentence\n- Torture or inhuman or degrading treatment\n- Serious threats against their life or integrity by reason of indiscriminate violence\nThese people will receive subsidiary protection If you find yourself in any of the aforementioned situations and you need protection from the Spanish authorities, you must submit a request for international protection\nSubmission of a request will result an evaluation of both situations by the Spanish authorities\nWHERE CAN I REQUEST INTERNATIONAL PROTECTION? - If you arrive in Spain but you cannot enter Spanish territory, at border control\n- If you are already in Spain: - At the Oficina de Asilo y Refugio (OAR) (Office of Asylum and Refuge)\n- In any Foreign Office\n- In authorised Police Stations\n- In Foreigner Internment Centres\nWHEN SHOULD I APPLY FOR INTERNATIONAL PROTECTION? - If you are on Spanish territory, within a period of ONE MONTH from your entry into Spain or from the moment the events justifying your request begin\nHOW DO I REQUEST INTERNATIONAL PROTECTION? - You must submit an application in person\nIf you cannot do this for physical or legal reasons, you may authorise another person to do it on your behalf\nYou will have to attend an interview in which you must answer a series of questions regarding your personal data, and in which you must explain all the reasons for which you are applying for international protection and how you arrived in Spain\nThe interview will be conducted by a manager who will tell you what to do and help you to complete it in order to establish all the relevant facts\nWHAT RIGHTS DOES AN APPLICANT FOR INTERNATIONAL PROTECTION HAVE? If you apply for international protection at the Spanish border or within Spanish Territory, you will have the following rights: - To remain in Spain until your application is resolved, notwithstanding any claim from another the EU country or from an International Criminal Court\n- To be assisted by an attorney, free of charge if you cannot pay (Bar Association or NGO)\n- To be assisted by an interpreter in the language of your choice\n- That your application be communicated to the United Nations High Commissioner for Refugees (UNHCR) in Spain\n- To have access to the content of your file at any time\n- To be documented as an applicant for international protection\n- To medical care to receive healthcare services, if needed\nWHAT ARE THE APPLICANT'S OBLIGATIONS? - Collaborate with the Spanish authorities: - Telling the truth about your identity, presenting any identification documents you have or, where applicable, justifying the absence thereof\n- Explaining in detail the reasons for which you are applying for international protection\n- Submitting any information to support your application, as soon as possible\n- Informing or appearing before the authorities whenever necessary in relation to your application, renewal of documents, etc\n- Reporting any change of address\nIf you do not report your new address, you may not receive correspondence in relation to your application for international protection, which may then be placed on file\n- Allowing your fingerprints to be taken\nIT IS ESSENTIAL THAT YOU CONFIDE IN THE SPANISH AUTHORITIES\nREMEMBER: - In order to help you, they need to know all about your situation\n- If you do not give true reasons for submitting your application for international protection from the start, or if any documentation you submit is not genuine, any explanations you give later on may lose credibility\n- Everything you say is CONFIDENTIAL\nYour country's government will never find out that you have applied for international protection in Spain nor be informed of anything you say\n- Every person you meet (officials, police, interpreters) is obligated to keep everything you say confidential\n- The persons you meet are used to working with people who need protection\nTrust them\n- You may contact the UNHCR or NGOs at any time\n- You have the right to be assisted by a lawyer, free of charge if you cannot pay, throughout the procedure\nWHAT DOES THE INTERNATIONAL PROTECTION PROCEDURE INVOLVE? 1\nINITIAL PROCESSING In this phase, any applications which do not correspond to Spain but to another EU country are not admitted, as are those which are repetitions of previous applications, or those submitted by nationals of other Member States\nIF YOU HAVE SUBMITTED YOUR APPLICATION ON SPANISH TERRITORY - You will be notified within one month as to whether your application has been admitted or not and, if admitted, if an urgent procedure will be applied\n- If your application is not admitted for processing you must leave Spain, unless you are authorised to stay\n- If your application is not admitted you may appeal to the courts\nIF YOU HAVE SUBMITTED YOUR APPLICATION AT THE SPANISH BORDER: 1\nYou must remain there until a decision has been made regarding your application\nThe authorities must make a decision within FOUR days\nIf your application is admitted, you may enter Spain\nIf your application is not admitted or is rejected, you MAY REQUEST A RE-EXAMINATION OF YOUR CASE (called a case review) within TWO DAYS from the moment you are informed of the non\u00ad admittance\nThe authorities will have TWO DAYS to respond\nIf the appeal is rejected, you must leave Spain\nYou may submit an appeal against a decision of non-admittance or rejection of your request before a judge or tribunal\nIf you have submitted your application for international protection at a Foreigner Internment Centre (CIE), it will be processed according to points three and five\nIf your application is admitted, it will be processed through the urgent procedure\nELIGIBILITY PROCESS - If your application is admitted for processing either at the border or within Spanish territory, it will be passed on for a thorough examination\n- The Authorities will have a maximum of SIX MONTHS, or THREE months when following URGENT procedure, to make a decision\n- During this phase, you may be summoned for another interview\n- If a decision is not made within SIX MONTHS, you will be informed as to the reasons for the delay\n- If the application is accepted, you will be recognised as a refugee or as a person under subsidiary protection\n- If it is rejected, you must leave Spain, unless you have any type of residency permit\n- You may submit an appeal against a negative decision before the Spanish Court (Audiencia Nacional)\nRemember that you are entitled to legal assistance, which will be free of charge if you cannot pay, during all phases of the procedure and for filing appeals\nWHO DECIDES OVER INTERNATIONAL PROTECTION APPLICATIONS? - All applications, regardless of who submits them, are examined by the Office of Asylum and Refuge\n- Decisions are made by the Ministry of the Interior\n- For decisions on applications admitted for processing, the Ministry of the Interior decides at the proposal of the lnterministerial Commission for Asylum and Refuge\nWHAT RIGHTS ARE GRANTED WITH INTERNATIONAL PROTECTION? - Not to be returned to your country of origin\n- Authorisation to live and work in Spain\n- Obtain an identification document and, where applicable, travel document\n- Reuniting with immediate family\n- Access to public employment services, education, healthcare, housing, welfare and social services, programs for victims of gender-based violence, social security, integration programs, further education and apprenticeships, and procedures for gaining academic and professional titles under the same conditions as local nationals\n- Access to specific integration and voluntary return programs\n- Reduced waiting times to gain Spanish nationalisation for refugees\nSOCIAL PROGRAMS FOR INTERNATIONAL PROTECTION APPLICANTS AND REFUGEES - International protection applicants may benefit from assistance which guarantees coverage of their basic needs\nThey are also authorised to work if their request is admitted for processing and more than six months have elapsed since its submission without receiving a final decision\n- People under international protection may benefit from social services, education and healthcare provided by public administrations\n- You can obtain more information at the Social Work Department of the Ministry of Labour and Immigration in the Office for Asylum and Refuge or from any of the NGOs detailed below\nUSEFUL ADDRESSES OFFICE OF ASYLUM AND REFUGE OFICINA DE ASILO Y REFUGIO (OAR) Cl Pradillo, 40 - 28002 Madrid Tel\n: 91 537 21 70 - 060 Metro: Alfonso XIII [URL_1] Edita: Ministerio del Interior, Secretar\u00eda General T\u00e9cnica\nNIPO Papel: 126-16-009-9\nNIPO en l\u00ednea: 126-16-010-1\nDep\u00f3sito legal: M-19644-2016 SUBDIRECTORATE GENERAL FOR IMMIGRANT INTEGRATION SUBDIRECCI\u00d3N GENERAL DE INTEGRACI\u00d3N DE LOS INMIGRANTES Ministerio de Empleo y Seguridad Social Unidad de Trabajo Social en la Oficina de Asilo y Refugio UNITED NATIONS HIGH COMMISSIONER FOR REFUGEES (UNHCR) AL TO COMISIONADO DE LAS NACIONES UNIDAS PARA LOS REFUGIADOS (ACNUR) Avda\nGeneral Peron, 32, 2\u00b0 lzq\n- 28020 Madrid Tel\n: 91 556 36 49 135 03 Metro: Santiago Bernabeu http:l/www\nacnur\norg1 NON-GOVERNMENTAL ORGANISATIONS (NGOs) SPANISH RED CROSS CRUZ ROJA ESPAF:IOLA C/ Valdecanillas, 112 - 28037 Madrid Metro: Simancas Tel\n: 91 532 55 55 [URL_2] SPANISH COMMISSION FOR REFUGEE ASSISTANCE COMISl6N ESPAAOLA DE AYUDA AL REFUGIADO (CEAR) C/ Hnos\nGarc\u00eda Noblejas, 41 - 8\u00ba izq - 28037 Madrid Metro: Garc\u00eda Noblejas Tel\n: 91 555 06 98 / 29 08 [URL_3] ACCEM Plaza Sta\nM8 Soledad Torres Acosta, 2, 3\u00b0 - 28004 Madrid Tel\n: 91 532 74 7819 Metro: Callao [URL_4] INTERNATIONAL RESCUE RESCATE INTERNACIONAL Cl Luchana, 36, 4\u00b0 Dcha\n- 28010 Madrid Tel\n: 91 447 28 72129 60 Metro: Bilbao [URL_5] NOTE: IN FORMATION ON LOCAL NGOs WHICH PROVIDE ASSISTANCE TO APPLICANTS CAN BE FOUND AT INTERNATIONAL PROTECTION APPLICATION OFFICES\n", "labels": [[9, 14, "LOCATION"], [766, 773, "MISCELLANEOUS"], [918, 925, "MISCELLANEOUS"], [1003, 1008, "LOCATION"], [1030, 1037, "MISCELLANEOUS"], [1091, 1096, "LOCATION"], [1107, 1114, "MISCELLANEOUS"], [1118, 1133, "MISCELLANEOUS"], [1135, 1138, "MISCELLANEOUS"], [1141, 1147, "MISCELLANEOUS"], [1151, 1168, "MISCELLANEOUS"], [1187, 1193, "ORGANIZATION"], [1326, 1333, "MISCELLANEOUS"], [1395, 1400, "LOCATION"], [1364, 1373, "TIME"], [1478, 1491, "ORGANIZATION"], [1896, 1901, "LOCATION"], [1976, 1979, "ORGANIZATION"], [2188, 2195, "MISCELLANEOUS"], [2258, 2263, "LOCATION"], [2343, 2345, "ORGANIZATION"], [2461, 2476, "ORGANIZATION"], [2480, 2483, "ORGANIZATION"], [2598, 2643, "ORGANIZATION"], [2645, 2650, "ORGANIZATION"], [2655, 2660, "LOCATION"], [2903, 2910, "MISCELLANEOUS"], [3646, 3653, "MISCELLANEOUS"], [4098, 4103, "LOCATION"], [4359, 4364, "ORGANIZATION"], [4521, 4531, "ORGANIZATION"], [4631, 4636, "LOCATION"], [4652, 4654, "ORGANIZATION"], [4839, 4846, "MISCELLANEOUS"], [4887, 4896, "TIME"], [5078, 5083, "LOCATION"], [5232, 5239, "MISCELLANEOUS"], [5334, 5345, "ORGANIZATION"], [5374, 5383, "TIME"], [5493, 5496, "TIME"], [5565, 5573, "TIME"], [5634, 5645, "MISCELLANEOUS"], [5656, 5664, "TIME"], [5915, 5942, "ORGANIZATION"], [5944, 5947, "ORGANIZATION"], [6189, 6196, "MISCELLANEOUS"], [6297, 6307, "TIME"], [6312, 6324, "TIME"], [6475, 6485, "TIME"], [6689, 6694, "LOCATION"], [6807, 6820, "MISCELLANEOUS"], [6822, 6840, "MISCELLANEOUS"], [7145, 7155, "ORGANIZATION"], [7184, 7208, "ORGANIZATION"], [7270, 7294, "ORGANIZATION"], [7343, 7353, "ORGANIZATION"], [7514, 7519, "LOCATION"], [7622, 7628, "ORGANIZATION"], [8055, 8062, "MISCELLANEOUS"], [8355, 8375, "TIME"], [8563, 8578, "ORGANIZATION"], [8662, 8668, "ORGANIZATION"], [8838, 8849, "PERSON"], [8862, 8868, "LOCATION"], [8850, 8861, "EU_PHONE_NUMBER"], [8901, 8913, "PERSON"], [8929, 8952, "LOCATION"], [8874, 8893, "EU_PHONE_NUMBER"], [8914, 8921, "URI"], [8992, 9005, "EU_PHONE_NUMBER"], [9006, 9010, "PERSON"], [9020, 9033, "EU_PHONE_NUMBER"], [9238, 9254, "ORGANIZATION"], [9265, 9310, "ORGANIZATION"], [9312, 9317, "ORGANIZATION"], [9325, 9379, "ORGANIZATION"], [9381, 9386, "ORGANIZATION"], [9393, 9406, "PERSON"], [9415, 9418, "PERSON"], [9427, 9433, "LOCATION"], [9467, 9475, "PERSON"], [9476, 9484, "LOCATION"], [9439, 9459, "EU_PHONE_NUMBER"], [9496, 9501, "ORGANIZATION"], [9545, 9562, "ORGANIZATION"], [9563, 9572, "ORGANIZATION"], [9573, 9578, "ORGANIZATION"], [9579, 9583, "ORGANIZATION"], [9587, 9600, "LOCATION"], [9614, 9626, "LOCATION"], [9628, 9636, "LOCATION"], [9601, 9613, "EU_PHONE_NUMBER"], [9664, 9671, "MISCELLANEOUS"], [9672, 9682, "ORGANIZATION"], [9642, 9655, "EU_PHONE_NUMBER"], [9656, 9663, "URI"], [9761, 9776, "LOCATION"], [9798, 9810, "LOCATION"], [9812, 9827, "LOCATION"], [9863, 9868, "LOCATION"], [9869, 9874, "PERSON"], [9833, 9846, "EU_PHONE_NUMBER"], [9855, 9862, "URI"], [9879, 9903, "LOCATION"], [9919, 9925, "LOCATION"], [9954, 9960, "LOCATION"], [9969, 10011, "MISCELLANEOUS"], [10015, 10022, "LOCATION"], [9931, 9946, "EU_PHONE_NUMBER"], [9961, 9968, "URI"], [10044, 10050, "LOCATION"], [10083, 10089, "LOCATION"], [10200, 10210, "ORGANIZATION"], [10056, 10075, "EU_PHONE_NUMBER"], [10090, 10097, "URI"]], "meta": "Malaga - Asylum Request - Asylum_and_Employment_Informacion_solicitantes_Asilo_Ingles"}

def document_exists(meta):
    try:
        documents = Document.objects.filter(meta=meta)
        return len(documents) > 0
    except Exception as e:
        print(e)
        return False

def create_document(text, meta, project):
    document = Document()

    document.text = text
    document.meta = meta
    document.project = project

    document.save()


'''test_project = SequenceLabelingProject()
test_project.name = "test save new project"
test_project.description = "test save new project"
test_project.guideline = "Please write annotation guideline"
test_project.project_type = 'sequence to sequence'
test_project.save()'''

#documents = []

project = Project.objects.get(pk=1)
#document = Document.objects.filter(meta="test 2")
user = User.objects.get(pk=1)

if document_exists(datas['meta']):
    print('YES')
'''
doc = Document.objects.get(pk=3)
label = Label.objects.get(pk=1)
user = User.objects.get(pk=2)

role = Role.objects.get(name="annotator")

role_mapping = RoleMapping()

role_mapping.user = user
role_mapping.project = project
role_mapping.role = role

role_mapping.save()

annotation = SequenceAnnotation()
annotation.document = doc
annotation.label = label
annotation.start_offset = 0
annotation.end_offset = 4
annotation.user = user

annotation.save()

#print(len(documents))

doc = Document()
doc.text = "test 3"
doc.project = project
doc.meta = "test 3"
doc.save()'''

#print(len(document))





#documents = Document.objects.filter(project=project)
#print(len(documents))
#print('test api reached')
#project_list = Project.objects.all()


#storage.save(user)