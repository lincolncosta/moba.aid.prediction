# --------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------
# install if you do not have the packages in your R system

# uncomment the following line to install packages
# install.packages(c("mlr", "randomForest", "rpart", "e1071", "kknn", "partykit"))

# --------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------

library(mlr)
set.seed(42)

# ---------------------------------
# different datasets
# ---------------------------------

cat("- Reading datasets\n")
dataset1 = read.csv("../data/dataset_old_features.csv")
dataset2 = read.csv("../data/dataset_new_features.csv")
dataset3 = read.csv("../data/dataset_full.csv")

# ---------------------------------
# defining classification tasks
# ---------------------------------

cat("- Creating tasks\n")
task1 = makeClassifTask(id = "old_features",  data = dataset1[,-c(1,2)], target = "result")
task2 = makeClassifTask(id = "new_features",  data = dataset2[,-c(1,2)], target = "result")
task3 = makeClassifTask(id = "full_features", data = dataset3[,-c(1,2)], target = "result")
tasks = list(task1, task2, task3)

# ---------------------------------
# learning process
# ---------------------------------

cat("- Instantiating learners\n")
lrn.rf  = makeLearner("classif.randomForest", predict.type = "prob")
lrn.dt  = makeLearner("classif.rpart", predict.type = "prob")
lrn.svm = makeLearner("classif.svm", predict.type = "prob")
lrn.nb  = makeLearner("classif.naiveBayes", predict.type = "prob")
lrn.knn = makeLearner("classif.kknn", predict.type = "prob")
lrn.log = makeLearner("classif.logreg", predict.type = "prob")
learners   = list(lrn.rf, lrn.dt, lrn.svm, lrn.nb, lrn.knn, lrn.log)


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
  measures = measures, keep.pred = TRUE, models = TRUE, show.info = TRUE)

#showing reuslts
print(bmk)

# saving results
cat("- Saving results\n")
save(bmk, file = "./benchmarking_results.RData")

# --------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------
