from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool, ScrapeWebsiteTool


@CrewBase
class DevrelwriterCrew():
	"""Devrelwriter crew"""

	@agent
	def researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['researcher'],
			tools=[SerperDevTool()],
			verbose=True,
			llm="gpt-4o"
		)

	@agent
	def blog_chapter_writer(self) -> Agent:
		return Agent(
			config=self.agents_config['blog_chapter_writer'],
			verbose=True,
			llm="gpt-4o"
		)

	@agent
	def blog_writer(self) -> Agent:
		return Agent(
			config=self.agents_config['blog_writer'],
			tools=[ScrapeWebsiteTool()],
			verbose=True,
			llm="gpt-4o"
		)
	
	@agent
	def tweet_writer(self) -> Agent:
		return Agent(
			config=self.agents_config['tweet_writer'],
			verbose=True,
		)

	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['research_task'],
			agent=self.researcher()
		)

	@task
	def blog_chapter_writer_task(self) -> Task:
		return Task(
			config=self.tasks_config['chapter_writer_task'],
			agent=self.blog_chapter_writer()
		)

	@task
	def blog_writer_task(self) -> Task:
		return Task(
			config=self.tasks_config['blog_post_task'],
			agent=self.blog_writer()
		)

	@task
	def tweet_writer_task(self) -> Task:
		return Task(
			config=self.tasks_config['tweet_writer_task'],
			agent=self.tweet_writer()
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Devrelwriter crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)