# Semester 1 assignment 1

## About
This is the first of two assignments that you are to complete this semester. The assignments are very similar to learning module question; you will be presented with a set of questions and will need to develop a solution for each one. Note that assignments can't be repeated multiple times, though the attempt does not have to be completed in one block.

Both assignments use Pylint, so make sure your code works in vscode and passes the Precheck tests before you submit it by clicking Check!

Note that this assignment starts relativity simply, but the difficulty ramps up quickly. Ensure that you give yourself plenty of time give to try each question. You can seek help with the assignment in weekly lab sessions and the help sessions that are run over the mid semester break.

Tutors will try and help you, but will do this by often by asking you question, and guiding you through the requirements. They will refrain from directly reading and editing your code.

## Marking
Questions 1 through 5 are each worth 20 marks each. Questions 6 and 7 are optional extension questions, and have no marks attached to them.

## Project

### About Project
Te Reo Māori is one of the three official languages of Aotearoa, New Zealand. There is a massive increase in the number of students attempting to learn Te Reo in the modern era*.

 In this assignment we are going to write a basic program to help students learn to translate basic terms from English to Te Reo Māori.

* Ministry of Education statistics show an increase in English speaking students taking Te Reo Māori as a subject in NCEA

### Constraints
During this assignment we will be building up a program testing the ability of students to translate English terms Te reo Māori.

For our purposes, if a student translates well to ora or as Ora (with a capital O), we want to count that as correct.

### Process

The first thing we want to do is process some text so that we have some terms that we can ask a student to translate.

We want to process strings that contain English and Te Reo Māori terms from a string that looks like this

```python
string = """english,māori
New Zealand,Aotearoa
North Island,Te Ika-a-Māui
South Island,Te Waipounamu
Wellington,Te Whanganui a Tara
Christchurch,Ōtautahi
Hamilton,Kirikiriroa
Auckland,Tāmaki Makaurau"""
```

The first line is a header that states what order the translation is in, i.e english,māori or māori,english. Then following are anywhere from 1 to n lines, each with two word-groups separated by a comma.  A word-group has at least one word in it, with a word being the usual definition of a group of characters separated by white-space.

Your task is to write a function get_translations(string) that takes a string, like the line above, and returns a list of tuples. The first element of the tuple is the English word-group, and the second is the Te Reo Māori word-group.

So the result of the above string would be the list:

```python
[
  ('New Zealand', 'Aotearoa'),
  ('North Island', 'Te Ika-a-Māui'),
  ('South Island', 'Te Waipounamu'),
  ('Wellington', 'Te Whanganui a Tara'),
  ('Christchurch', 'Ōtautahi'),
  ('Hamilton', 'Kirikiriroa'),
  ('Auckland', 'Tāmaki Makaurau')
]
```

If one of the languages in the header is not recognized then print the error message:

'Header language not recognized!' and return an empty list. Note that at present we only support English and Te Reo Māori.

