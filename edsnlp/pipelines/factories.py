# flake8: noqa: F811
from .core.advanced.factory import create_component as advanced
from .core.context.factory import create_component as context
from .core.contextual_matcher.factory import create_component as contextual_matcher
from .core.endlines.factory import create_component as endlines
from .core.matcher.factory import create_component as matcher
from .core.normalizer.accents.factory import create_component as accents
from .core.normalizer.factory import create_component as normalizer
from .core.normalizer.lowercase.factory import remove_lowercase
from .core.normalizer.pollution.factory import create_component as pollution
from .core.normalizer.quotes.factory import create_component as quotes
from .core.sentences.factory import create_component as sentences
from .core.terminology.factory import create_component as terminology
from .misc.consultation_dates.factory import create_component as consultation_dates
from .misc.dates.factory import create_component as dates
from .misc.measurements.factory import create_component as measurements
from .misc.reason.factory import create_component as reason
from .misc.sections.factory import create_component as sections
from .ner.cim10.factory import create_component as cim10
from .ner.covid.factory import create_component as covid
from .ner.drugs.factory import create_component as drugs
from .ner.scores.charlson.factory import create_component as charlson
from .ner.scores.emergency.ccmu.factory import create_component as ccmu
from .ner.scores.emergency.gemsa.factory import create_component as gemsa
from .ner.scores.emergency.priority.factory import create_component as priority
from .ner.scores.factory import create_component as score
from .ner.scores.sofa.factory import create_component as sofa
from .ner.scores.tnm.factory import create_component as tnm
from .qualifiers.family.factory import create_component as family
from .qualifiers.history.factory import create_component as history
from .qualifiers.hypothesis.factory import create_component as hypothesis
from .qualifiers.negation.factory import create_component as negation
from .qualifiers.reported_speech.factory import create_component as rspeech
