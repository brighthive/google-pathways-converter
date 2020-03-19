# google-pathways-converter

The `google-pathways-converter` is a Python package that converts a dictionary of keyword arguments into a Google-pathways-friendly JSON-LD.  

## Motivation (Why did we build this?)
[Google Pathways](https://developers.google.com/search/docs/data-types/job-training), an online utility integrated with the Google search engine, illuminates "pathways" for job seekers trying to acquire skills for a new role, job, or career. Google  reads structured data from publicly available web pages, and if compatible with Pathways, the data appears in Google search results. Try it for yourself! Go to [Google](https://www.google.com/), and enter “job training and Richmond, VA”. You should see a panel with expandable results for jobs, paid training, and educational programs near Richmond. 

Google only ingests programs data that aligns with the specific schema definitions standardized by [schema.org](https://schema.org/). Schema.org specifies schemas for two program types: `WorkBasedProgram` or `EducationalOccupationalProgram`. A work-based program both provides job training and pays a wage. An educational-occupational program does not pay a wage, but offers a learning experience, which may or may not require the student to pay tuition and/or fees.

A BrightHive Data Trust may include data resources that describe work-based and/or educational-occupational programs. In many cases, Data Trust members want to easily, securely, and effectively disseminate information about their program offerings – something that Google Pathways facilitates. To this end, the `google-pathways-converter` transforms data resources into JSON-LD and makes it possible to integrate programs data with Google Pathways.

# DEMO
What does this tool do? Screenshots and GIFs.

# GETTING STARTED
How do I get this running on my machine locally?

# TESTING
`google-pathways-converter` comes with a comprehensive suite of unit tests. Execute all tests by running:

```
pipenv run pytest
```

# OTHER INFORMATION
Anything else the reader should know?

# HOW TO CONTRIBUTE
This section should provide instructions for making a contributions: 
opening a feature branch, using a PR template, tagging the appropriate BrightHive people, etc.

# TEAM

* Regina Compton (Software Engineer)
* Logan Ripplinger (Software Engineer)

https://brighthive.io/brighthive-team/