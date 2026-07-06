"""Single source of truth for the H446 course taxonomy and repo paths.

Every build script imports this — component/topic/subtopic names, stems and
the staging layout live here and nowhere else.
"""
import os

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = os.path.join(REPO, "zz_source", "revision-tools")
STAGE = os.path.join(REPO, "zz_source", "_staging")
STAGE_PDF = os.path.join(STAGE, "pdf")
STAGE_WORD = os.path.join(STAGE, "word")
STAGE_PPT = os.path.join(STAGE, "ppt")
STAGE_XL = os.path.join(STAGE, "xl")

# (Component title, [ (Topic title, topic-stem, [(Subtopic title, sub-stem)...]) ])
STRUCTURE = [
 ("Component 1 - Computer Systems", [
   ("1.1 Processors, Input, Output and Storage", "1.1-processors-input-output-storage", [
     ("1.1.1 Structure and Function of the Processor", "1.1.1-structure-and-function-of-the-processor"),
     ("1.1.2 Types of Processor", "1.1.2-types-of-processor"),
     ("1.1.3 Input, Output and Storage Devices", "1.1.3-input-output-and-storage-devices")]),
   ("1.2 Software and Software Development", "1.2-software-and-software-development", [
     ("1.2.1 Operating Systems", "1.2.1-operating-systems"),
     ("1.2.2 Applications Generation", "1.2.2-applications-generation"),
     ("1.2.3 Software Development", "1.2.3-software-development"),
     ("1.2.4 Types of Programming Language", "1.2.4-types-of-programming-language")]),
   ("1.3 Exchanging Data", "1.3-exchanging-data", [
     ("1.3.1 Compression, Encryption and Hashing", "1.3.1-compression-encryption-and-hashing"),
     ("1.3.2 Databases", "1.3.2-databases"),
     ("1.3.3 Networks", "1.3.3-networks"),
     ("1.3.4 Web Technologies", "1.3.4-web-technologies")]),
   ("1.4 Data Types, Data Structures and Boolean Algebra", "1.4-data-types-structures-boolean-algebra", [
     ("1.4.1 Data Types", "1.4.1-data-types"),
     ("1.4.2 Data Structures", "1.4.2-data-structures"),
     ("1.4.3 Boolean Algebra", "1.4.3-boolean-algebra")]),
   ("1.5 Legal, Moral, Cultural and Ethical Issues", "1.5-legal-moral-cultural-ethical", [
     ("1.5.1 Computing Related Legislation", "1.5.1-computing-related-legislation"),
     ("1.5.2 Moral and Ethical Issues", "1.5.2-moral-and-ethical-issues")]),
 ]),
 ("Component 2 - Algorithms and Programming", [
   ("2.1 Elements of Computational Thinking", "2.1-elements-of-computational-thinking", [
     ("2.1.1 Thinking Abstractly", "2.1.1-thinking-abstractly"),
     ("2.1.2 Thinking Ahead", "2.1.2-thinking-ahead"),
     ("2.1.3 Thinking Procedurally", "2.1.3-thinking-procedurally"),
     ("2.1.4 Thinking Logically", "2.1.4-thinking-logically"),
     ("2.1.5 Thinking Concurrently", "2.1.5-thinking-concurrently")]),
   ("2.2 Problem Solving and Programming", "2.2-problem-solving-and-programming", [
     ("2.2.1 Programming Techniques", "2.2.1-programming-techniques"),
     ("2.2.2 Computational Methods", "2.2.2-computational-methods")]),
   ("2.3 Algorithms", "2.3-algorithms", [
     ("2.3.1 Algorithms", "2.3.1-algorithms")]),
 ]),
]

# subtopic code ("1.1.1") -> full stem; and code -> display title
SUB_STEM, SUB_TITLE, TOPIC_OF = {}, {}, {}
TOPIC_STEM, TOPIC_TITLE = {}, {}
for _comp, _topics in STRUCTURE:
    for _ttitle, _tstem, _subs in _topics:
        _tcode = _ttitle.split()[0]
        TOPIC_STEM[_tcode] = _tstem
        TOPIC_TITLE[_tcode] = _ttitle
        for _stitle, _sstem in _subs:
            _code = _stitle.split()[0]
            SUB_STEM[_code] = _sstem
            SUB_TITLE[_code] = _stitle
            TOPIC_OF[_code] = _tcode

# Subtopics NOT taught in the Year 12 SOW (they ship in the Topic Library
# marked Year 13 rather than in a weekly folder).
YEAR13_SUBTOPICS = ["1.5.1", "1.5.2", "2.2.2", "2.3.1"]


def code_of(stem):
    """'1.3.1-compression-...' -> '1.3.1'; '1.3-exchanging-data' -> '1.3'."""
    return stem.split("-")[0]
