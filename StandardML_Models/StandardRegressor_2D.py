
class StandardRegressor_2D:

    def __init__(self, model_name, **model_params):
        self.model_name = model_name
        self.model = None
        if self.model_name == 'KNN':
            from sklearn.neighbors import KNeighborsRegressor
            self.model1 = KNeighborsRegressor(**model_params)
            self.model2 = KNeighborsRegressor(**model_params)
        elif self.model_name == 'LinearReg':
            from sklearn.linear_model import LinearRegression
            self.model1 = LinearRegression(**model_params)
            self.model2 = LinearRegression(**model_params)
        elif self.model_name == 'Ridge':
            from sklearn.linear_model import Ridge
            self.model1 = Ridge(**model_params)
            self.model2 = Ridge(**model_params)
        elif self.model_name == 'Lasso':
            from sklearn.linear_model import Lasso
            self.model1 = Lasso(**model_params)
            self.model2 = Lasso(**model_params)
        elif self.model_name == 'ElasticNet':
            from sklearn.linear_model import ElasticNet
            self.model1 = ElasticNet(**model_params)
            self.model2 = ElasticNet(**model_params)
        elif self.model_name == 'RBF SVR':
            from sklearn.svm import SVR
            self.model1 = SVR(**model_params)
            self.model2 = SVR(**model_params)
        elif self.model_name == 'DecisionTree':
            from sklearn.tree import DecisionTreeRegressor
            self.model1 = DecisionTreeRegressor(**model_params)
            self.model2 = DecisionTreeRegressor(**model_params)
        elif self.model_name == 'RandomForest':
            from sklearn.ensemble import RandomForestRegressor
            self.model1 = RandomForestRegressor(**model_params)
            self.model2 = RandomForestRegressor(**model_params)
        elif self.model_name == 'GradientBoost':
            from sklearn.ensemble import GradientBoostingRegressor
            self.model1 = GradientBoostingRegressor(**model_params)
            self.model2 = GradientBoostingRegressor(**model_params)
        elif self.model_name == 'AdaBoost':
            from sklearn.ensemble import AdaBoostRegressor
            self.model1 = AdaBoostRegressor(**model_params)
            self.model2 = AdaBoostRegressor(**model_params)
        elif self.model_name == 'XGBoost':
            from xgboost import XGBRegressor
            self.model1 = XGBRegressor(**model_params)
            self.model2 = XGBRegressor(**model_params)

    def fit(self, trainX, trainY, validX, validY):
        trainX = trainX.reshape((-1, 258))  # TODO: A hack for now
        self.model1.fit(trainX, trainY[:,0].ravel())
        self.model2.fit(trainX, trainY[:,1].ravel())

    def predict(self, testX):
        testX = testX.reshape((-1, 258))  # TODO: A hack for now
        predict1 = self.model1.predict(testX)
        predict2 = self.model2.predict(testX)
        return [predict1, predict2]
