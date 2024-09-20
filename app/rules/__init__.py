from .accessibility_terms.accessibility_terms import check_accessibility_terms
from .ai_bot_terms.ai_bot_terms import check_ai_bot_terms
from .cloud_computing_terms.cloud_computing_terms import check_cloud_computing_terms
from .computer_device_terms.computer_device_terms import check_computer_device_terms
from .date_time_terms.date_time_terms import check_date_time_terms
from .keys_keyboard_shortcuts.keys_keyboard_shortcuts import check_keys_keyboard_shortcuts
from .mouse_interaction_terms.mouse_interaction_terms import check_mouse_interaction_terms
from .security_terms.security_terms import check_security_terms
from .special_characters.special_characters import check_special_characters
from .touch_pen_interaction_terms.touch_pen_interaction_terms import check_touch_pen_interaction_terms
from .units_of_measure_terms.units_of_measure_terms import check_units_of_measure_terms
from .dimensional_terms.dimensional_terms import check_dimensional_terms
from .terminology_usage import check_terminology_usage
from .style_formatting import check_style_formatting
from .grammar_word_choice import check_grammar_word_choice
from .terminology_b_terms import check_terminology_b_terms
from .style_formatting_b_terms import check_style_formatting_b_terms
from .technical_terms import check_technical_terms
from .grammar_word_choice_b_terms import check_grammar_word_choice_b_terms
from .c.c_languages_terms import check_c_languages_terms
from .c.cable_terms import check_cable_terms
from .c.cabling_terms import check_cabling_terms
from .c.cache_terms import check_cache_terms
from .c.calendar_terms import check_calendar_terms
from .c.callback_terms import check_callback_terms
from .c.callout_terms import check_callout_terms
from .c.can_may_terms import check_can_may_terms
from .c.cancel_terms import check_cancel_terms

rule_functions = [
    check_accessibility_terms,
    check_ai_bot_terms,
    check_cloud_computing_terms,
    check_computer_device_terms,
    check_date_time_terms,
    check_keys_keyboard_shortcuts,
    check_mouse_interaction_terms,
    check_security_terms,
    check_special_characters,
    check_touch_pen_interaction_terms,
    check_units_of_measure_terms,
    check_dimensional_terms,
    check_terminology_usage,
    check_style_formatting,
    check_grammar_word_choice,
    check_terminology_b_terms,
    check_style_formatting_b_terms,
    check_technical_terms,
    check_grammar_word_choice_b_terms, 
    check_c_languages_terms,
    check_cable_terms,
    check_cabling_terms,
    check_cache_terms,
    check_calendar_terms,
    check_callback_terms,
    check_callout_terms, 
    check_can_may_terms,
    check_cancel_terms
]

__all__ = ['rule_functions']

