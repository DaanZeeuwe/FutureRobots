from experimentation.experiment import ExperimentFactory


class Simulation:

    def __init__(self, n: int = 100):
        self.experiment_factory = ExperimentFactory()
        self.n = n

    def simulate(self):
        experiment = self.experiment_factory.create()

        for i in range(self.n):
            experiment.step()

        print(experiment.robots)


if __name__ == "__main__":
    s = Simulation()
    s.simulate()
