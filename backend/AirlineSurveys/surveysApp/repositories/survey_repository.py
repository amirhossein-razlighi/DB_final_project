from ..models import Survey, Question, Multichoicequestion, Choice , Chooses ,Answers , Takesurvey , Voter  , Descriptivequestion
from ..util.decorators import log_error



@log_error
def insert_takesurvey(survey_id ,user_id , start_time)  :
    survey =  Survey.objects.get( surveyid = survey_id )
    voter =  Voter.objects.get ( userid = user_id)
    takesurvey = Takesurvey(
    voterid = voter , 
    surveyid = survey ,
    starttime = start_time )
    takesurvey.save()


@log_error
def insert_answers_text( voter_id , survey_id ,question_number , ans ) :
    survey =   Descriptivequestion.objects.get( surveyid = survey_id , questionnumber  = question_number )
    voter =  Takesurvey.objects.get ( voterid = voter_id) 
    answer = Answers( 
    voterid =  voter, 
    surveyid  = survey,
    questionnumber  = question_number,
    answertext = ans 
    )
    answer.save()



@log_error
def insert_choice_answer( voter_id ,  survey_id , question_number  , choice) : 
    survey =   Multichoicequestion.objects.get( surveyid = survey_id , questionnumber  = question_number )
    choicesid =  Choice.objects.get ( surveyid =survey , questionnumber  = question_number  , choicenumber  = choice  )
    
    voter =  Takesurvey.objects.get ( voterid = voter_id )  
    choice_answer = Chooses( 
    voterid =  voter, 
    surveyid  = choicesid , 
    questionnumber  = question_number ,
    choicenumber = choice 
    )
    choice_answer.save()





@log_error
def get_question(survey_id, question_number):
    question = Question.objects.get(surveyid=survey_id, questionnumber=question_number)
    choices = []
    try:
        multi_choice = Multichoicequestion.objects.get(questionid=question)
        question_choices = Choice.objects.filter(survey_id=survey_id, question_number=question_number)
        for choice in question_choices:
            choices.append({
                'choice_number': choice.choicenumber,
                'choice_text': choice.choicetext
            })

    except Exception as e:
        pass
    return {
        "question_number": question.questionnumber,
        "choices": choices
    }


@log_error
def get_answers_by_questionnum( survey_id , question_number ) :
    Answers = []
    question = Question.objects.get(surveyid=survey_id, questionnumber= question_number)

    try : 
        answers_by_number = Answers.objects.filter(surveyid=survey_id ,questionnumber =  question_number)
        for ans in answers_by_number  : 
          Answers.append( {  "is_descriptive"  : True , "question_nummber" : question_number  ,"question_text"  : question.questiontext  , "answer" :  ans.answertext } )
    except Exception as e : 
        Chooses_by_number =  Chooses.objects.filter ( surveyid=survey_id ,questionnumber =  question_number)  
        choices = []
        question_choices = Choice.objects.filter(survey_id=survey_id, question_number=question_number)
        for choice in question_choices:
            choices.append({
                'choice_number': choice.choicenumber,
                'choice_text': choice.choicetext
            }) 
        for ans in Chooses_by_number :  
            Answers.append( {   "is_descriptive"  : False , "question_nummber" : question_number  ,"question_text"  : question.questiontext  , "choices" :  choices , "answer" : ans.choicenumber } )

    return  Answers         




@log_error
def get_questions_by_survey_id(survey_id):
    questions = Question.objects.filter(surveyid=survey_id)
    questions_info = []
    for question in questions:
        choices = []
        try:
            multi_choice = Multichoicequestion.objects.get(questionid=question)
            question_choices = Choice.objects.filter(survey_id=survey_id, question_number=question.questionnumber)
            for choice in question_choices:
                choices.append({
                    'choice_number': choice.choicenumber,
                    'choice_text': choice.choicetext
                })

        except Exception as e:
            pass
        questions_info.append({
            "question_number": question.questionnumber,
            "choices": choices
        })
    return questions_info


@log_error
def get_survey(survey_id):
    return Survey.objects.get(surveyid=survey_id)


@log_error
def find_by_airline_id(airline_id):
    return Survey.objects.filter(airlineid=airline_id)

