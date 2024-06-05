import flet as ft

class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleAnalizza(self, e):
        threshold = self._view._txtIn.value
        try:
            float(threshold)
        except ValueError:
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(ft.Text("Please provide a numerical value for distance. "))
            self._view.update_page()
            return

        self._model.buildGraph(float(threshold))

        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(ft.Text("Graph created!"))
        self._view._txt_result.controls.append(ft.Text("Num of nodes:" + str(self._model.getNumNodes())))
        self._view._txt_result.controls.append(ft.Text("Num of edges:" + str(self._model.getNumEdges())))
        allEdges = self._model.getAllEdges()
        for edge in allEdges:
            self._view._txt_result.controls.append(
                ft.Text(f"{edge[0]}->{edge[1]} -- AvgDist: {self._model.getAvgDist(edge[0], edge[1])}"))

        self._view.update_page()
