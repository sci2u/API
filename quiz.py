import random
from xml.dom import minidom

from question import QuestionBase, AnswerBase


class QuizQuestionBase(QuestionBase):
    def is_correct_answer(self, answer):
        """
        Returns True if answer is a correct answer to
        this question, False otherwise.
        """
        raise NotImplementedError('QuizQuestion must implement is_correct_answer()')
    
    def most_favorable_answer(self, answer1, answer2):
        """
        Decide whether answer1 or answer2 is most favorable
        as an answer to this question.
        
        Returns -1 if answer1 is more favorable than answer2.
        Returns 0 if answer1 and answer2 are equal.
        Returns 1 if answer1 is less favorable than answer2.
        """
        if self.is_correct_answer(answer1) and self.is_correct_answer(answer2):
            apr1 = self.correct_answer_proximate(answer1)
            apr2 = self.correct_answer_proximate(answer2)
            if apr1 > apr2:
                return -1
            elif apr1 < apr2:
                return 1
            else:
                return random.choice([-1, 1])            
        elif self.is_correct_answer(answer1):
            return -1
        elif self.is_correct_answer(answer2):
            return 1
        
        apr1 = self.proximate(answer1) 
        apr2 = self.proximate(answer2)
        
        if apr1 > apr2:
            return -1
        elif apr1 < apr2:
            return 1
        else:
            return random.choice([-1, 1])
    
    def favorized_answers(self, all_answers):
        """
        Given a large set of answers, this method returns a sorted list
        of answers, where the first elements (answers) are the most favored.
        Do not edit the original list 'all_answers' - in stead create a new!
        """
        return sorted(all_answers, cmp=self.most_favorable_answer)
    
    def pick_answers(self, all_answers):
        """
        Picks answers for this question.
        """
        picked_answers = []
        num_answers = self.num_answers_nomalized()
        max_sim = self.max_similarity()
        max_ans = self.maximum_correct_answers()
        
        # Pick questions that are not too similar
        # Give a copy of the list to favorized_answers, so the
        # method can't mutate the all_answers.

        num_correct_ans = 0
        for answer in self.favorized_answers(list(all_answers)):
            is_too_similar = False
            is_not_too_correct = True
            
            for a in picked_answers:
                if a.similarity(answer) > max_sim:
                    is_too_similar = True
                    break            

            if self.is_correct_answer(answer):
                is_not_too_correct = num_correct_ans < max_ans
                if is_not_too_correct:
                    num_correct_ans += 1
            
            if not is_too_similar and is_not_too_correct:
                picked_answers.append(answer)
            
            if len(picked_answers) == num_answers:
                self.number_of_correct_answers = num_correct_ans                    
                break

            
        return sorted(picked_answers[:num_answers])
    
    def validate_answers(self, picked_answers):
        """
        Check whether question has enough correct answers.
        Raises an exception if it doesn't.
        """
        correct_required = self.required_correct_answers()
        correct_answers = [a for a in picked_answers if 
                            self.is_correct_answer(a)]
        
        if len(correct_answers) < correct_required:
            raise RuntimeError('Question does not have enough correct answers: %s \n (%s found, %s required)' % (
                                                            str(self),
                                                            str(len(correct_answers)),
                                                            str(correct_required)))


class QuizAnswerBase(AnswerBase):
    pass


class QuizXMLReport(object):
    def __init__(self, sort_questions_randomly):
        self._doc = minidom.Document()
        self._root = self._doc.createElement('root')
        self._root.setAttribute('type', 'quiz')
        self._root.setAttribute('sort_questions_randomly',
                                '1' if sort_questions_randomly else '0')
        self._doc.appendChild(self._root)
    
    def add_question(self, question, answers):
        """
        Add a question and its answers to the report.
        """
        q = self._doc.createElement('question')
        q.setAttribute('filename', question._filename)
        req_corr_ans = question.required_correct_answers()
        if req_corr_ans == 0:
            req_corr_ans = question.number_of_correct_answers                           
        q.setAttribute('required_correct_answers', 
                       str(req_corr_ans))
        q.setAttribute('sort_answers_randomly', 
                       '1' if question.sort_answers_randomly() else '0')
        
        # Write answers
        for i, answer in enumerate(sorted(answers)):
            a = self._doc.createElement('answer')
            a.setAttribute('filename', answer._filename)
            a.setAttribute('sort', str(i))
            a.setAttribute('is_correct',
                           '1' if question.is_correct_answer(answer) else '0')
            q.appendChild(a)
        
        self._root.appendChild(q)
    
    def save(self, to_file):
        with open(to_file, 'w') as f:
            xml_str = self._doc.toprettyxml(indent='  ')
            f.write(xml_str)
