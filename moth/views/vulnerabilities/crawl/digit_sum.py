import random

from django.http import Http404
from django.shortcuts import render

from moth.views.base.html_template_view import HTMLTemplateView
from moth.views.base.vulnerable_template_view import VulnerableTemplateView

PARAGRAPHS = {
    20: [
        "Weary with toil, I haste me to my bed,",
        "The dear repose for limbs with travel tired;",
        "But then begins a journey in my head,",
        "To work my mind, when body’s work’s expired:",
        "For then my thoughts (from far where I abide)",
        "Intend a zealous pilgrimage to thee,",
        "And keep my drooping eyelids open wide,",
        "Looking on darkness which the blind do see:",
        "Save that my soul’s imaginary sight",
        "Presents thy shadow to my sightless view,",
        "Which, like a jewel hung in ghastly night,",
        "Makes black night beauteous and her old face new.",
        "Lo, thus, by day my limbs, by night my mind,",
        "For thee, and for myself, no quiet find."
    ],
    21: [
        "Shall I compare thee to a summer’s day?",
        "Thou art more lovely and more temperate.",
        "Rough winds do shake the darling buds of May,",
        "And summer’s lease hath all too short a date.",
        "Sometime too hot the eye of heaven shines,",
        "And often is his gold complexion dimmed;",
        "And every fair from fair sometime declines,",
        "By chance or nature’s changing course untrimmed.",
        "But thy eternal summer shall not fade,",
        "Nor lose possession of that fair thou ow’st,",
        "Nor shall Death brag thou wand’rest in his shade,",
        "When in eternal lines to time thou grow’st.",
        "So long as men can breathe or eyes can see,",
        "So long lives this, and this gives life to thee."
    ],
    22: [
        "Let me not to the marriage of true minds",
        "Admit impediments; love is not love",
        "Which alters when it alteration finds,",
        "Or bends with the remover to remove.",
        "O no, it is an ever-fixed mark",
        "That looks on tempests and is never shaken;",
        "It is the star to every wandering bark,",
        "Whose worth’s unknown, although his height be taken.",
        "Love’s not Time’s fool, though rosy lips and cheeks",
        "Within his bending sickle’s compass come;",
        "Love alters not with his brief hours and weeks,",
        "But bears it out even to the edge of doom.",
        "If this be error and upon me proved,",
        "I never writ, nor no man ever loved."
    ],
    23: [
        "To me, fair friend, you never can be old,",
        "For as you were when first your eye I eyed,",
        "Such seems your beauty still. Three winters cold",
        "Have from the forests shook three summers’ pride,",
        "Three beauteous springs to yellow autumn turned",
        "In process of the seasons have I seen,",
        "Three April perfumes in three hot Junes burned,",
        "Since first I saw you fresh, which yet are green.",
        "Ah, yet doth beauty, like a dial hand,",
        "Steal from his figure and no pace perceived;",
        "So your sweet hue, which methinks still doth stand,",
        "Hath motion and mine eye may be deceived;",
        "For fear of which, hear this, thou age unbred:",
        "Ere you were born was beauty’s summer dead."
    ]
}

class FileSeedView(HTMLTemplateView):
    title = 'Seed file for digit-sum process'
    description = 'Just an initial file with numbers for digit-sum to work on.'
    url_path = 'index-3-1.html'

    HTML = '''
    Seed for the digit sum process.
    '''

class FileTargetView(HTMLTemplateView):
    title = 'Target file for digit-sum process'
    tags = ['not-linked']
    description = 'Target with numbers for digit-sum to identify.'
    url_path = 'index-2-1.html'
    linked = False

    HTML = '''
    Target for the digit sum process.
    '''

def lorem_ipsum_paragraphs(id):
    return PARAGRAPHS[id]

class QsDigitsView(VulnerableTemplateView):
    title = 'Digit sum query string'
    tags = ['query-string', 'GET']
    description = 'Test file for digit sum. Content differs when changing ids.'\
                  ' Valid ids are 20, 21, 22 and 23.'
    url_path = 'index1.py?id=20'

    VALID_IDS = [20, 21, 22, 23]

    def get(self, request, *args, **kwds):
        context = self.get_context_data()

        _id = request.GET['id']

        if _id.isdigit() and int(_id) in self.VALID_IDS:
            context['html'] = '<br><br>'.join(lorem_ipsum_paragraphs(int(_id))) * ((int(_id) - 19) * 5)
        else:
            raise Http404

        return render(request, self.template_name, context)

