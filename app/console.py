import pdb

from models.race_result import Race_result
import repositories.race_result_repository as race_result_repository

from models.runner import Runner
import repositories.runner_repository as runner_repository

from models.race import Race
import repositories.race_repository as race_repository


race_result_repository.delete_all()
runner_repository.delete_all()
race_repository.delete_all()

runner_1 = Runner("Steven", "McFarlane")
runner_repository.save(runner_1)
runner_2 = Runner("Joanna", "McFarlane")
runner_repository.save(runner_2)
runner_3 = Runner("Vito", "Corleone")
runner_repository.save(runner_3)
runner_4 = Runner("Malcolm", "Tucker")
runner_repository.save(runner_4)
runner_5 = Runner("Jimmy", "Garroppolo")
runner_repository.save(runner_5)
runner_6 = Runner("Eddie", "Vedder")
runner_repository.save(runner_6)
runner_7 = Runner("Sabrina", "Pace")
runner_repository.save(runner_7)
runner_8 = Runner("Jasmine", "Paris")
runner_repository.save(runner_8)
runner_9 = Runner("Emilie", "Forsberg")
runner_repository.save(runner_9)

race_1 = Race("Dumyat Dash", '2020-08-28', 6.2, 457)
race_repository.save(race_1)
race_2 = Race("Cockelroy", '2020-01-01', 3.4, 132)
race_repository.save(race_2)
race_3 = Race("Ochil 2000s", '2020-11-28', 33.0, 1200)
race_repository.save(race_3)
race_4 = Race("EPIC Trail 10K", '2021-01-30', 10, 421)
race_repository.save(race_4)

# race_time_1 = Race_time(race_1, runner_1, 32)
# race_time_repository.save(race_time_1)

race_result_1 = Race_result(race_1, runner_2, 42)
race_result_repository.save(race_result_1)
race_result_2 = Race_result(race_1, runner_1, 43)
race_result_repository.save(race_result_2)
race_result_3 = Race_result(race_1, runner_3, 32)
race_result_repository.save(race_result_3)
race_result_4 = Race_result(race_1, runner_4, 37)
race_result_repository.save(race_result_4)
race_result_5 = Race_result(race_1, runner_7, 33)
race_result_repository.save(race_result_5)
race_result_6 = Race_result(race_1, runner_8, 31)
race_result_repository.save(race_result_6)
race_result_7 = Race_result(race_1, runner_9, 24)
race_result_repository.save(race_result_7)

race_result_8 = Race_result(race_2, runner_4, 18)
race_result_repository.save(race_result_8)
race_result_9 = Race_result(race_2, runner_5, 9)
race_result_repository.save(race_result_9)
race_result_10 = Race_result(race_2, runner_9, 12)
race_result_repository.save(race_result_10)
race_result_11 = Race_result(race_2, runner_8, 10)
race_result_repository.save(race_result_11)
race_result_12 = Race_result(race_2, runner_1, 14)
race_result_repository.save(race_result_12)
race_result_13 = Race_result(race_2, runner_6, 12)
race_result_repository.save(race_result_13)
race_result_14 = Race_result(race_2, runner_2, 11)
race_result_repository.save(race_result_14)

pdb.set_trace()