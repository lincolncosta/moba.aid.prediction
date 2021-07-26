# --------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------
# install if you do not have the packages in your R system

# uncomment the following line to install packages
# install.packages(c("mlr", "randomForest", "rpart", "e1071", "kknn", "partykit"),
#   repos = "http://cran.us.r-project.org")

# --------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------

library(mlr)
set.seed(42)

# ---------------------------------
# different datasets
# ---------------------------------

cat("- Reading datasets\n")
dataset1 = read.csv("../data/dataset_picked_champions.csv")
dataset2 = read.csv("../data/dataset_players_statistics.csv")
dataset3 = read.csv("../data/dataset_picked_champions_players_statistics.csv")
dataset4 = read.csv("../data/dataset_banned_champions.csv")
dataset5 = read.csv("../data/dataset_full.csv")

# ---------------------------------
# defining classification tasks
# ---------------------------------

cat("- Creating tasks\n")
task1 = makeClassifTask(id = "picked_champions",  data = dataset1[,-1], target = "result")
task2 = makeClassifTask(id = "players_statistics",  data = dataset2[,-1], target = "result")
task3 = makeClassifTask(id = "picked_champions_players_statistics", data = dataset3[,-1],
  target = "result")
task4 = makeClassifTask(id = "banned_champions",  data = dataset4[,-1], target = "result")
task5 = makeClassifTask(id = "full",  data = dataset5[,-1], target = "result")

tasks = list(task1, task2, task3, task4, task5)

# ---------------------------------
# learning process
# ---------------------------------

cat("- Instantiating learners\n")
lrn.rf  = makeLearner("classif.randomForest", predict.type = "prob", id="RandomForest")
lrn.dt  = makeLearner("classif.rpart", predict.type = "prob", id="Rpart")
lrn.svm = makeLearner("classif.svm", predict.type = "prob", id="SVM")
lrn.nb  = makeLearner("classif.naiveBayes", predict.type = "prob", id="NaiveBayes")
lrn.knn = makeLearner("classif.kknn", predict.type = "prob", id="KKNN")
lrn.log = makeLearner("classif.logreg", predict.type = "prob", id="LogReg")
learners   = list(lrn.dt, lrn.svm, lrn.nb, lrn.knn, lrn.log, lrn.rf)

cat("- Defining Measures and resampling\n")
measures   = list(auc, bac, f1)

# for debug
# resampling = makeResampleDesc(method = "CV", stratify = TRUE, iter = 10)
resampling = makeResampleDesc(method = "RepCV", rep = 5, folds = 10, stratify = TRUE)

# ---------------------------------
# benchmarking
# ---------------------------------

cat("- Benchmarking\n")
bmk = benchmark(tasks = tasks, learners = learners, resamplings = resampling,
  measures = measures, keep.pred = FALSE, models = TRUE, show.info = TRUE)

#showing reuslts
print(bmk)

# saving results
cat("- Saving results\n")
save(bmk, file = "./benchmarking_results.RData")

# --------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------
