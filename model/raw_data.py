from langchain_core.documents import Document

documents = [
    # ARTICLE 1 -- DEFINITIONS
    Document(
        page_content="Academic staff is staff members at the level of Assistant Professor, Associate Professor or Full Professor and lecturers (docent) with a PhD degree.",
        metadata={"page": "5", "article": "1.2", "article_name": "definitions", "document_name": "rules and regulation",
                  "section": "1", "section_name": "general provisions", "iid": 1},
    ),
    Document(
        page_content="Assessment committee is committee tasked with providing expert advice on assessment",
        metadata={"page": "5", "article": "1.2", "article_name": "definitions", "document_name": "rules and regulation",
                  "section": "1", "section_name": "general provisions", "iid": 2},
    ),
    Document(
        page_content="Assessment plan is plan describing the assessment of a component",
        metadata={"page": "5", "article": "1.2", "article_name": "definitions", "document_name": "rules and regulation",
                  "section": "1", "section_name": "general provisions", "iid": 3},
    ),
    Document(
        page_content="DACS is Department of Advanced Computing Sciences",
        metadata={"page": "5", "article": "1.2", "article_name": "definitions", "document_name": "rules and regulation",
                  "section": "1", "section_name": "general provisions", "iid": 4},
    ),
    Document(
        page_content="Exam component is part of the exam of a component/course. This can also be a practical or an assignment.",
        metadata={"page": "5", "article": "1.2", "article_name": "definitions", "document_name": "rules and regulation",
                  "section": "1", "section_name": "general provisions", "iid": 5},
    ),
    Document(
        page_content="Force majeure is events and associated consequences that are abnormal, beyond the control of the student, and where the student had no way of preventing the negative consequences nor were the events and consequences within the sphere of risk of the student",
        metadata={"page": "5", "article": "1.2", "article_name": "definitions", "document_name": "rules and regulation",
                  "section": "1", "section_name": "general provisions", "iid": 6},
    ),
    Document(
        page_content="Student portal is the electronic environment for providing information to students including intranet and Canvas",
        metadata={"page": "5", "article": "1.2", "article_name": "definitions", "document_name": "rules and regulation",
                  "section": "1", "section_name": "general provisions", "iid": 7},
    ),
    Document(
        page_content="Teaching team is all persons involved in teaching the component",
        metadata={"page": "5", "article": "1.2", "article_name": "definitions", "document_name": "rules and regulation",
                  "section": "1", "section_name": "general provisions", "iid": 8},
    ),

    # ARTICLE 3.7 HARDSHIP
    Document(
        page_content="In cases where the application of the regulations would lead to manifestly unreasonable results (The student must adhere to the deadline for the submission of the thesis plan for the given semester), due to personal circumstances, the following applies:",
        metadata={"page": "18", "article": "3.7", "article_name": "hardship", "document_name": "rules and regulation",
                  "section": "3", "section_name": "procedures", "iid": 9},
    ),
    Document(
        page_content="The Board of Examiners decides whether circumstances are hardship or not. When students make a request for hardship the student must properly motivate this request and provide proof for the circumstances that have occurred. The request must be filed as soon as possible, but no later than two weeks after the event occurred. a. Without proper proof the claim cannot be taken into consideration. To be clear: An email claiming illness is not considered proof. b. If it is possible to avoid a problem from occurring by e.g. requesting to reschedule a meeting, the student is obliged to do so.",
        metadata={"page": "18", "article": "3.7", "article_name": "hardship", "document_name": "rules and regulation",
                  "section": "3", "section_name": "procedures", "iid": 10},
    ),
    Document(
        page_content="For the Board of Examiners to take a hardship request into consideration, the student must show force majeure for all opportunities. Examples that might be considered as hardship: a. Acute medical care that made it impossible to participate and there was no alternative available b. Death of a family member in the first degree that made it impossible to participate and there was no alternative available",
        metadata={"page": "18", "article": "3.7", "article_name": "hardship", "document_name": "rules and regulation",
                  "section": "3", "section_name": "procedures", "iid": 11},
    ),
    Document(
        page_content="Examples that are not considered hardship: a. Plannable medical care b. Seeking medical care, available in the Netherlands, abroad c. Motivation d. Study delay or financial issues e. Exchange f. Consequences of fraud g. Travel",
        metadata={"page": "18 & 19", "article": "3.7", "article_name": "hardship",
                  "document_name": "rules and regulation", "section": "3", "section_name": "procedures", "iid": 12},
    ),
    Document(
        page_content="In cases of personal circumstances students are obliged to be proactive and seek help from the study advisor and actively try to mitigate the possible effects.",
        metadata={"page": "19", "article": "3.7", "article_name": "hardship", "document_name": "rules and regulation",
                  "section": "3", "section_name": "procedures", "iid": 13},
    ),
    Document(
        page_content="Written exams are organised twice per year, which does not imply that the student has the right to have two exam attempts per year. As such, the choice of not taking the first opportunity is to be avoided and bears additional risk.",
        metadata={"page": "19", "article": "3.7", "article_name": "hardship", "document_name": "rules and regulation",
                  "section": "3", "section_name": "procedures", "iid": 14},
    ),

    # Section 7 -- ARTICLE 7.13 SKILL CLASSES
    Document(
        page_content="Mandatory skill classes can be imposed. Failure to attend or participate in the complete training has the consequence that the honours certificate is withheld.",
        metadata={"page": "29", "article": "7.13", "article_name": "skill classes",
                  "document_name": "rules and regulation", "section": "7", "section_name": "project skill classes",
                  "iid": 15},
    ),

    # ARTICLE 5.1 -- APPLICABILITY OF THE RULES AND REGULATIONS
    Document(
        page_content="This section describes the rules and regulations specific to the semester projects of the Bachelor’s programme in Data Science & Artificial Intelligence, withstanding the Education and Examination Regulations, hereinafter referred to as EERs. These project regulations apply only for a semester project, not for group assignments within a course.",
        metadata={"page": "20", "article": "5.1", "article_name": "applicability of the rules and regulations",
                  "document_name": "rules and regulation", "section": "5",
                  "section_name": "semester project regulations", "iid": 16},
    ),

    # ARTICLE 5.2 -- DEFINITIONS
    # I didn't add the this part, it didn't seem to be useful: "The definitions stated in Article 1.2 of the EER and in Article 1.2 of these Rules and Regulations apply. In addition, the following definitions apply:

    Document(
        page_content="Project content examiner(s) is the person(s) who sets the requirements for the different aspects of the project, assesses the content of the project including product, presentation, report and process, and provides content-based supervision during the projects.",
        metadata={"page": "20", "article": "5.2", "article_name": "definitions",
                  "document_name": "rules and regulation", "section": "5",
                  "section_name": "semester project regulations", "iid": 17},
    ),
    Document(
        page_content="project is an education component, as defined in Article 7.13(2)(t) of the act, where students work in small groups on complex and challenging assignments in order to develop a variety of skills. A project spreads out over one semester (or multiple blocks). They are usually group projects, but individual projects may also occur.",
        metadata={"page": "20", "article": "5.2", "article_name": "definitions",
                  "document_name": "rules and regulation", "section": "5",
                  "section_name": "semester project regulations", "iid": 18},
    ),
    Document(
        page_content="project group is a small group of students that jointly work on a project. Project groups can also consist of a single member.",
        metadata={"page": "20", "article": "5.2", "article_name": "definitions",
                  "document_name": "rules and regulation", "section": "5",
                  "section_name": "semester project regulations", "iid": 19},
    ),
    Document(
        page_content="Project coordinato is the person responsible for the daily management of a project semester as a whole, and acts as an examiner as the coordinator awards the results within the legal framework.",
        metadata={"page": "20", "article": "5.2", "article_name": "definitions",
                  "document_name": "rules and regulation", "section": "5",
                  "section_name": "semester project regulations", "iid": 20},
    ),
    Document(
        page_content="project tutor is the person responsible for the daily management of a project group in a certain semester or certain block during a semester.",
        metadata={"page": "20", "article": "5.2", "article_name": "definitions",
                  "document_name": "rules and regulation", "section": "5",
                  "section_name": "semester project regulations", "iid": 21},
    ),
    Document(
        page_content="project manual is study resource for the project. The project manual contains the project assignment.",
        metadata={"page": "20", "article": "5.2", "article_name": "definitions",
                  "document_name": "rules and regulation", "section": "5",
                  "section_name": "semester project regulations", "iid": 22},
    ),
    Document(
        page_content="project meeting is an educational activity, as defined in Article 7.13(2)(t) of the act; a scheduled meeting of the project group aimed at learning project management. The project tutor joins in during part of the meeting and assess the process.",
        metadata={"page": "20", "article": "5.2", "article_name": "definitions",
                  "document_name": "rules and regulation", "section": "5",
                  "section_name": "semester project regulations", "iid": 23},
    ),
    Document(
        page_content="skills training is an educational activity, as defined in Article 7.13(2)(t) of the act; skills training that is part of the project as referred to as “project skill” in the EER.",
        metadata={"page": "20", "article": "5.2", "article_name": "definitions",
                  "document_name": "rules and regulation", "section": "5",
                  "section_name": "semester project regulations", "iid": 24},
    ),
    # ARTICLE 5.3 -- ORGANIZATION
    Document(
        page_content="The project coordinator is responsible for the daily management of the project; regularly communicates and coordinates the project examiners; is responsible for the attendance and participation registration for the compulsory project meetings (which are indicated in the project manual or in these regulations); manages the project tutor(s), administers assessment, ensures that the students are given feedback and coordinates with the project content examiners the composition of the project manual and distributes information at the start of the project.",
        metadata={"page": "20", "article": "5.3", "article_name": "organization",
                  "document_name": "rules and regulation", "section": "5",
                  "section_name": "semester project regulations", "iid": 25},
    ),
    Document(
        page_content="The project tutor(s) supervise the students using a process-based approach and, if necessary and expertise permitting, also a content-based approach. Students regularly report back to the project tutors during the project meetings. The project tutor(s) track the attendance and participation of students during project meetings.",
        metadata={"page": "20", "article": "5.3", "article_name": "organization",
                  "document_name": "rules and regulation", "section": "5",
                  "section_name": "semester project regulations", "iid": 26},
    ),
    Document(
        page_content="Projects are group work and all students are expected to actively participate. Students whose behaviour is still detrimental after receiving a formal warning can be expelled from the project and receive an NG. They are not allowed to take a project resit.",
        metadata={"page": "20", "article": "5.3", "article_name": "organization",
                  "document_name": "rules and regulation", "section": "5",
                  "section_name": "semester project regulations", "iid": 27},
    ),
    Document(
        page_content="Students that have failed or have been expelled from a particular semester project in at least two different years, can be placed in special project groups at the discretion of the Director of Studies, while abiding to the learning outcomes. ",
        metadata={"page": "21", "article": "5.3", "article_name": "organization",
                  "document_name": "rules and regulation", "section": "5",
                  "section_name": "semester project regulations", "iid": 28},
    ),
    Document(
        page_content="It is up to the examiners to decide which student will present what in the project presentations, and this decision can be communicated by the examiners last-minute. The first and second phase presentations are in principle non-public (unless the examiners decide otherwise), the final presentation is a public presentation.",
        metadata={"page": "21", "article": "5.3", "article_name": "organization",
                  "document_name": "rules and regulation", "section": "5",
                  "section_name": "semester project regulations", "iid": 29},
    ),
    ## Article 5.4 -- ATTENDANCE AND PARTICIPATION
    Document(
        page_content="On-campus attendance and participation in the project meetings and project skills trainings, is mandatory, see Article 4.4 of the EER. Missing a meeting or training in this article means failure to be present during part of or the complete meeting or training, inadequate participation or inadequately completing the assignments. For project meetings the project tutor or project coordinator decides whether a student missed it or not, and for the skill trainings the lecturer or project coordinator.",
        metadata={"page": "21", "article": "5.4", "article_name": "attendance and participation",
                  "document_name": "rules and regulation", "section": "5",
                  "section_name": "semester project regulations", "related_articles": "Article 4.4", "iid": 30},
    ),
    Document(
        page_content="All project meetings are mandatory. One project meeting may be missed each block of the three blocks of a semester, without consequences, as an arrangement to cover force majeure and may only be used as such. If two or more meetings are missed in the first or second block of the semester, the student will not have access to the exam of that project phase and that phase will count as grade zero. If two meetings are missed in the third block of the semester, the student will automatically receive a lowered individual grade. If three or more meetings are missed in the third block of the semester, the student will not have access to the exam of that project phase and that phase will count as grade zero.",
        metadata={"page": "21", "article": "5.4", "article_name": "attendance and participation",
                  "document_name": "rules and regulation", "section": "5",
                  "section_name": "semester project regulations", "iid": 31},
    ),
    Document(
        page_content="Participation in project skill trainings is taken into account in the final grading. If a student has missed three or more skills trainings, the student will not be able to participate in the final examination of the project, meaning that an NG is given for the project. This NG will also be awarded if after the final examination it turns out that a student that was ineligible still participated.",
        metadata={"page": "21", "article": "5.4", "article_name": "attendance and participation",
                  "document_name": "rules and regulation", "section": "5",
                  "section_name": "semester project regulations", "iid": 32},
    ),
    Document(
        page_content="The arrangements that offer the possibility to miss project meetings and skill classes should not be taken lightly and only be used in a case of clear force majeure.",
        metadata={"page": "21", "article": "5.4", "article_name": "attendance and participation",
                  "document_name": "rules and regulation", "section": "5",
                  "section_name": "semester project regulations", "iid": 33},
    ),

    ## Article 5.5 -- EXAMINERS
    Document(
        page_content="The Board of Examiners appoints at least two project content examiners and a project coordinator, where the role of project content examiner and coordinator can be combined. The project examiners determine the grade according to a pre-agreed procedure and set extra assignments when needed. The tutor provides advice on the assessments of the project management as part of the final assessment. The project coordinator adjusts the individual grades as described in Article 5.4 and Article 5.6 and hands the final grades in to the exam administration.",
        metadata={"page": "21", "article": "5.5", "article_name": "attendance and participation",
                  "document_name": "rules and regulation", "section": "5",
                  "section_name": "semester project regulations", "iid": 34},
    ),

    ## Article 5.6 -- PROJECT GRADE
    Document(
        page_content="The project is graded on three occasions by the examiners. The first grade is issued after the presentation first phase and accounts for 15% of the final grade. The second grade is issued after the presentation second phase and accounts for 15% of the final grade. The third grade is issued after the final assessment at the end of the third block and accounts for 70% of the grade. These grades are then rescaled in Paragraph 5 to a range 0 to 9.",
        metadata={"page": "21 & 22", "article": "5.6", "article_name": "project grade",
                  "document_name": "rules and regulation", "section": "5",
                  "section_name": "semester project regulations", "iid": 35},
    ),
    Document(
        page_content="The skill trainings are graded on a scale from 0 to 1.",
        metadata={"page": "22", "article": "5.6", "article_name": "project grade",
                  "document_name": "rules and regulation", "section": "5",
                  "section_name": "semester project regulations", "iid": 36},
    ),
    # Different splits for ^^ in a-d. Seperated documents: vvv
    Document(
        page_content="If a student has participated fully in all skill classes, where the student also has a passing grade for all assignments, the student will receive the grade of 1 for the skill trainings.",
        metadata={"page": "22", "article": "5.6", "article_name": "skill class grade",
                  "document_name": "rules and regulation", "section": "5",
                  "section_name": "semester project regulations", "iid": 37},
    ),
    Document(
        page_content="If a student has participated fully in all but one skill trainings, where fully participating includes that the student has a passing grade for all assignments, the student will receive a grade of 0.5 for the skill classes.",
        metadata={"page": "22", "article": "5.6", "article_name": "skill class grade",
                  "document_name": "rules and regulation", "section": "5",
                  "section_name": "semester project regulations", "iid": 38},
    ),
    Document(
        page_content="If the student fully participated in all but two skill trainings, the student will receive a grade of 0.0 for the skill trainings.",
        metadata={"page": "22", "article": "5.6", "article_name": "skill class grade",
                  "document_name": "rules and regulation", "section": "5",
                  "section_name": "semester project regulations", "iid": 39},
    ),
    Document(
        page_content="If the student did not participate fully in three or more skill trainings, the student will not be able to participate in the final examination of the project, meaning that an NG is given for the project.",
        metadata={"page": "22", "article": "5.6", "article_name": "skill class grade",
                  "document_name": "rules and regulation", "section": "5",
                  "section_name": "semester project regulations", "iid": 40},
    ),
    # Different splits for ^^ in a-d ENDED ^^^

    # INSERTION:
    Document(
        page_content="As indicated in paragraph 1, for each project there are a number of on-campus assessment moments that may include, but are not limited to: the presentation first phase, the presentation second phase, the final presentation and the product and report examination (if applicable).",
        metadata={"page": "22", "article": "5.6", "article_name": "project grade",
                  "document_name": "rules and regulation", "section": "5",
                  "section_name": "semester project regulations", "iid": 41},
    ),
    Document(
        page_content="Failure to participate in either the presentation first phase or presentation second phase has the consequence that the student concerned cannot be graded for that particular phase and the grade for that phase will count as 0.",
        metadata={"page": "22", "article": "5.6", "article_name": "project grade",
                  "document_name": "rules and regulation", "section": "5",
                  "section_name": "semester project regulations", "iid": 42},
    ),
    Document(
        page_content="Failure to participate in the final project presentation means that the student cannot be graded for the presentation and the grade for the rubrics concerning the presentation will count as 0.",
        metadata={"page": "22", "article": "5.6", "article_name": "project grade",
                  "document_name": "rules and regulation", "section": "5",
                  "section_name": "semester project regulations", "iid": 43},
    ),
    Document(
        page_content="If a student does not participate in the product and report examination (if applicable), there is insufficient bases for assessing the individual contribution of the student, with the consequence that an NG is awarded for the overall project of the student involved.",
        metadata={"page": "22", "article": "5.6", "article_name": "project grade",
                  "document_name": "rules and regulation", "section": "5",
                  "section_name": "semester project regulations", "iid": 44},
    ),
    Document(
        page_content="If a student misses in total two or more of the aforementioned assessment moments (e.g. the presentation first phase, the presentation second phase, the final presentation and the product and report examination (if applicable)), there is insufficient bases for assessing the individual contribution of the student, with the consequence that an NG is awarded for the overall project of the student involved.",
        metadata={"page": "22", "article": "5.6", "article_name": "project grade",
                  "document_name": "rules and regulation", "section": "5",
                  "section_name": "semester project regulations", "iid": 45},
    ),
    # INSERTION END

    Document(
        page_content="The final assessment will be determined at the end of each project. Each project will be assessed separately and will be based on the following aspects: the project report; the project product; the project presentation; participation; project management and coorperation; the grades from earlier project phases. The requirements for the project product, report and presentations are determined separately for each project and will be listed in the project manual or on the Student Portal.",
        metadata={"page": "22", "article": "5.6", "article_name": "project grade",
                  "document_name": "rules and regulation", "section": "5",
                  "section_name": "semester project regulations", "iid": 46},
    ),
    Document(
        page_content="The project grade is on a scale from 0 to 10, where the grade consists for 90% of the grade from paragraph 1, to which the skill class grade is added.",
        metadata={"page": "22", "article": "5.6", "article_name": "project grade",
                  "document_name": "rules and regulation", "section": "5",
                  "section_name": "semester project regulations", "iid": 47},
    ),
    Document(
        page_content="The project grade is a group grade, which applies to all members of the group. The project examiners may deviate (positively or negatively) from the group grade and issue an individual grade for students, if participation and cooperation within a group has not been homogeneous.",
        metadata={"page": "22", "article": "5.6", "article_name": "project grade",
                  "document_name": "rules and regulation", "section": "5",
                  "section_name": "semester project regulations", "iid": 48},
    ),
    Document(
        page_content="Examiners can choose to use peer assessment for adjusting individual grades.",
        metadata={"page": "22", "article": "5.6", "article_name": "project grade",
                  "document_name": "rules and regulation", "section": "5",
                  "section_name": "semester project regulations", "iid": 49},
    ),
    Document(
        page_content="For students who have not met the project requirements by insufficient participation in project meetings, skill trainings, project presentations, the product and report examination (if applicable) and any other mandatory meetings, the modification to the student’s grade as indicated in Article 5.4 and in Article 5.6.3 will be applied after the individual grading of the student.",
        metadata={"page": "22", "article": "5.6", "article_name": "project grade",
                  "document_name": "rules and regulation", "section": "5",
                  "section_name": "semester project regulations", "iid": 50},
    ),

    ## Article 5.7 -- PROJECT RESULTS: WRITTEN MOTIVATION
    Document(
        page_content="The project assessment will be motivated in writing on a form that provides an overview of the project report, product and presentations and shows to what degree the results fulfil the final requirements for the project.",
        metadata={"page": "23", "article": "5.7", "article_name": "project results: written motivation",
                  "document_name": "rules and regulation", "section": "5",
                  "section_name": "semester project regulations", "iid": 51},
    ),

    ## Article 5.8 -- RESITS
    Document(
        page_content="The resit is a repair opportunity, and the method shall be determined by the examiners. Repair opportunities can be individual or on a group level, where changes will be permitted to the composition of the original project group. Students who were expelled from the project or did not receive a grade in the current academic year are not allowed to take the project resit. A repair opportunity will only be offered if the grade is 4.0 or more (hence an NG is ineligible for a resit) to ensure that a student has obtained sufficient practical training. The student(s) will receive the resit assignment from the examiners within 2 working days after failing the project. This additional assignment must be handed in within 10 working days. If completed successfully, the student will receive a 6.0 for the project.",
        metadata={"page": "23", "article": "5.8", "article_name": "project resits",
                  "document_name": "rules and regulation", "section": "5",
                  "section_name": "semester project regulations", "iid": 52},
    ),

    ## Article 5.8 -- HARDSHIP
    Document(
        page_content="The Board of Examiners can excuse students from the participation in project meetings in individual cases due to personal circumstances and can offer repair opportunities for the project as a whole. The student must in such cases prove force majeure for all mandatory meeting that the student missed, see also Article 3.7 of the Rules and Regulations. Deviation from the group grade is possible in such cases. The Board of Examiners can also grant resits for projects in special circumstances. Since the project is an onsite group activity, students must be within commuting distance from Maastricht during each project activity.",
        metadata={"page": "23", "article": "5.9", "article_name": "project hardship",
                  "document_name": "rules and regulation", "section": "5",
                  "section_name": "semester project regulations", "iid": 53},
    ),
    # Different splits for ^^ in a-y. Seperated documents: vvv
    Document(
        page_content=" Student is a person who is registered at the university for education and/or to take exams and the examination of the programme;",
        metadata={"page": "3", "article": "1.2", "article_name": "definitions",
                  "document_name": "education and examination regulation", "section": "1",
                  "section_name": "general provisions", "iid": 54},
    ),
    Document(
        page_content="Component is a study unit of the programme within the meaning of the Act;",
        metadata={"page": "3", "article": "1.2", "article_name": "definitions",
                  "document_name": "education and examination regulation", "section": "1",
                  "section_name": "general provisions", "iid": 55},
    ),
    Document(
        page_content="Course is a component of at most 4 ECTS, consisting of lectures and tutorials.",
        metadata={"page": "3", "article": "1.2", "article_name": "definitions",
                  "document_name": "education and examination regulation", "section": "1",
                  "section_name": "general provisions", "iid": 56},
    ),
    Document(
        page_content="Propaedeutic phase is the initial period for the programme with a study load of 60 credits, coinciding with course year 1;",
        metadata={"page": "3", "article": "1.2", "article_name": "definitions",
                  "document_name": "education and examination regulation", "section": "1",
                  "section_name": "general provisions", "iid": 57},
    ),
    Document(
        page_content="Course year is year 1, year 2 or year 3 of the programme;",
        metadata={"page": "3", "article": "1.2", "article_name": "definitions",
                  "document_name": "education and examination regulation", "section": "1",
                  "section_name": "general provisions", "iid": 58},
    ),
    Document(
        page_content="Academic year is the period from 1 September of a calendar year up to and including 31 August of the following calendar year;",
        metadata={"page": "3", "article": "1.2", "article_name": "definitions",
                  "document_name": "education and examination regulation", "section": "1",
                  "section_name": "general provisions", "iid": 59},
    ),
    Document(
        page_content="Programme is the bachelor’s programme referred to in Article 1.1 of these regulations, consisting of a coherent whole of study units;",
        metadata={"page": "3", "article": "1.2", "article_name": "definitions",
                  "document_name": "education and examination regulation", "section": "1",
                  "section_name": "general provisions", "iid": 60},
    ),
    Document(
        page_content="Exam is a component of the examination as referred to in Article 7.10 of the Act;",
        metadata={"page": "3", "article": "1.2", "article_name": "definitions",
                  "document_name": "education and examination regulation", "section": "1",
                  "section_name": "general provisions", "iid": 61},
    ),
    Document(
        page_content="Practical / Skill is practical exercise as referred to in Article 7.13(2)(d) of the Act, in one of the following forms: - writing a thesis; - carrying out a (group) project; - performing a research assignment; - developing a software program; - writing a paper, creating a technological design or performing another written assignment; - participating in field work or a field trip; - completing an internship; - participating in project skill classes - participating in project meetings - tutorial",
        metadata={"page": "3", "article": "1.2", "article_name": "definitions",
                  "document_name": "education and examination regulation", "section": "1",
                  "section_name": "general provisions", "iid": 62},
    ),
    Document(
        page_content="Examination is the final examination for the bachelor’s programme;",
        metadata={"page": "3", "article": "1.2", "article_name": "definitions",
                  "document_name": "education and examination regulation", "section": "1",
                  "section_name": "general provisions", "iid": 63},
    ),
    Document(
        page_content="Written exam is a summative assessment that constitutes or is part of an exam, consisting of multiple choice or open questions performed either on paper or in a digital format.",
        metadata={"page": "4", "article": "1.2", "article_name": "definitions",
                  "document_name": "education and examination regulation", "section": "1",
                  "section_name": "general provisions", "iid": 64},
    ),
    Document(
        page_content="Credit is a unit expressed in ECTS credits, with one credit equalling 28 hours of study;",
        metadata={"page": "4", "article": "1.2", "article_name": "definitions",
                  "document_name": "education and examination regulation", "section": "1",
                  "section_name": "general provisions", "iid": 65},
    ),
    Document(
        page_content="Educational Programme Committee is the representation and advisory body that carries out the duties described in Article 9.18 and 9.38c of the Act;",
        metadata={"page": "4", "article": "1.2", "article_name": "definitions",
                  "document_name": "education and examination regulation", "section": "1",
                  "section_name": "general provisions", "iid": 66},
    ),
    Document(
        page_content="Examiner is the person designated by the Board of Examiners to administer exams and to determine the results of such exams;",
        metadata={"page": "4", "article": "1.2", "article_name": "definitions",
                  "document_name": "education and examination regulation", "section": "1",
                  "section_name": "general provisions", "iid": 67},
    ),
    Document(
        page_content="Negative Binding Study Advice is the advice in accordance with Article 7.8b of the Act entailing that the student cannot continue in the programme;",
        metadata={"page": "4", "article": "1.2", "article_name": "definitions",
                  "document_name": "education and examination regulation", "section": "1",
                  "section_name": "general provisions", "iid": 68},
    ),
    Document(
        page_content="Semester is part of an academic year, either starting first of September and running for 20 educational weeks, or starting first of February running for 21 educational weeks;",
        metadata={"page": "4", "article": "1.2", "article_name": "definitions",
                  "document_name": "education and examination regulation", "section": "1",
                  "section_name": "general provisions", "iid": 69},
    ),
    Document(
        page_content="Block is part of a semester during which educational activities take place;",
        metadata={"page": "4", "article": "1.2", "article_name": "definitions",
                  "document_name": "education and examination regulation", "section": "1",
                  "section_name": "general provisions", "iid": 70},
    ),
    Document(
        page_content="DSAI is Data Science and Artificial Intelligence;",
        metadata={"page": "4", "article": "1.2", "article_name": "definitions",
                  "document_name": "education and examination regulation", "section": "1",
                  "section_name": "general provisions", "iid": 71},
    ),
    Document(
        page_content="DACS is Department of Advanced Computing Sciences;",
        metadata={"page": "4", "article": "1.2", "article_name": "definitions",
                  "document_name": "education and examination regulation", "section": "1",
                  "section_name": "general provisions", "iid": 72},
    ),
    Document(
        page_content="UM is Maastricht University;",
        metadata={"page": "4", "article": "1.2", "article_name": "definitions",
                  "document_name": "education and examination regulation", "section": "1",
                  "section_name": "general provisions", "iid": 73},
    ),
    Document(
        page_content="BSA Committee is the committee that issues the (negative) Binding Study Advice on behalf of the Faculty Board;",
        metadata={"page": "4", "article": "1.2", "article_name": "definitions",
                  "document_name": "education and examination regulation", "section": "1",
                  "section_name": "general provisions", "iid": 74},
    ),
    Document(
        page_content="Study guide is the programme guide, which includes further details about programme-specific provisions and information.",
        metadata={"page": "4", "article": "1.2", "article_name": "definitions",
                  "document_name": "education and examination regulation", "section": "1",
                  "section_name": "general provisions", "iid": 75},
    ),
    # Article 4.4 Attendance, participation, and best-efforts obligation
    Document(
        page_content="Attendance and participation at project skill trainings and project meetings is mandatory. In addition, each student is required to participate actively in doing tasks with respect to the project and to cooperate actively with their group in order to successfully finish the project assignment.",
        metadata={"page": "11", "article": "4.4",
                  "article_name": "attendance, participation, and best-efforts obligation",
                  "document_name": "education and examination regulation", "section": "4", "section_name": "education",
                  "iid": 76},
    ),
    Document(
        page_content="The requirements in paragraph 1 are requirements as in article 7.13(2)(t) of the act. A student who has not met the requirements as stated in paragraph 1, cannot participate in the examination of the project and will receive an NG. More information can be found in the Rules and Regulations.",
        metadata={"page": "11", "article": "4.4",
                  "article_name": "attendance, participation, and best-efforts obligation",
                  "document_name": "education and examination regulation", "section": "4", "section_name": "education",
                  "iid": 77},
    ),
    Document(
        page_content="Students whose absence or inactivity during the project has been marked as inexcusable by the project coordinator, and/or students that have a substandard contribution to the group work will not receive a pass for the project concerned.",
        metadata={"page": "11", "article": "4.4",
                  "article_name": "attendance, participation, and best-efforts obligation",
                  "document_name": "education and examination regulation", "section": "4", "section_name": "education",
                  "iid": 78},
    ),
    Document(
        page_content="Attendance and participation in other education activities may be part of an exam when announced in the study guide or Student Portal/the digital learning environment. Prior approval of the Board of Examiners is required.",
        metadata={"page": "11", "article": "4.4",
                  "article_name": "attendance, participation, and best-efforts obligation",
                  "document_name": "education and examination regulation", "section": "4", "section_name": "education",
                  "iid": 79},
    ),
    # Article 8.3 Unforeseen cases/safety net scheme
    Document(
        page_content="In cases not covered or not clearly covered by these regulations, decisions are taken by or on behalf of the Faculty Board, after it has consulted with the Board of Examiners.",
        metadata={"page": "19", "article": "8.3", "article_name": "unforeseen cases/safety net scheme",
                  "document_name": "education and examination regulation", "section": "8",
                  "section_name": "transitional and final provisions", "iid": 80},
    ),
    Document(
        page_content="In individual cases in which application of the Education and Examination Regulations, except for the study advice rules, would lead to manifestly unreasonable results, the Board of Examiners candeviate from the stated regulations in the student’s favour.",
        metadata={"page": "19", "article": "8.3", "article_name": "unforeseen cases/safety net scheme",
                  "document_name": "education and examination regulation", "section": "8",
                  "section_name": "transitional and final provisions", "iid": 81},
    ),
]
