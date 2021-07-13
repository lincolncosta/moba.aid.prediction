# --------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------
# install if you do not have the packages in your R system

# uncomment the following line to install packages
# install.packages(c("ggplot2", "PMCMR", "PMCMRplus", "dplyr"),
# repos = "http://cran.us.r-project.org")

library(mlr)
library(ggplot2)

# --------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------

dir.create("../plots/", showWarnings = FALSE)

# loading data
cat("- Loading data\n")
load(file = "./benchmarking_results.RData") #bmk

# --------------------------------------------------------------------------------------------------
# boxplots
# --------------------------------------------------------------------------------------------------
cat("- Boxplots from mlr\n")

g1 = plotBMRBoxplots(bmk, measure = auc)
ggsave(g1, file = "../plots/bench_auc.pdf", width = 7.97, height = 5.01)

g2 = plotBMRBoxplots(bmk, measure = bac)
ggsave(g2, file = "../plots/bench_bac.pdf", width = 7.97, height = 5.01)

g3 = plotBMRBoxplots(bmk, measure = f1)
ggsave(g3, file = "../plots/bench_f1.pdf", width = 7.97, height = 5.01)

# --------------------------------------------------------------------------------------------------
# Rf feature importance
# --------------------------------------------------------------------------------------------------

tasks = c("picked_champions", "players_statistics", "picked_champions_players_statistics",
  "banned_champions", "full")

# repeating the analysis for all the datasets
for(task in tasks) {

  cat("RF feature importance for: ", task, "\n")

  rf.models = mlr::getBMRModels(bmr=bmk, learner.ids = "RandomForest",
    task.ids = task, drop = TRUE)

  # feature importance
  aux = lapply(rf.models, function(mdl) {
    obj = mlr::getLearnerModel(mdl)
    return(obj$importance)
  })
  avg.imp = Reduce("+", aux)/length(aux)

  df = data.frame(avg.imp)
  df$feature = rownames(df)
  rownames(df) = NULL

  #ordering the factors
  df = df[order(df$MeanDecreaseGini, decreasing=TRUE),]
  df$feature = factor(df$feature, levels = df$feature)

  # bar plot
  g = ggplot(df, mapping = aes(x = feature, y = MeanDecreaseGini))
  g = g + geom_bar(stat = "identity", fill = "black") + theme_bw()
  g = g + theme(axis.text.x = element_text(angle = 90, vjust = .5, hjust = 1))

  ggsave(g, file = paste0("../plots/rf_feature_importance_", task, "_.pdf"),
    width = 6.89, height = 3.04)
}

# --------------------------------------------------------------------------------------------------
# Plot critical difference test for a selected measure
# --------------------------------------------------------------------------------------------------

cat("- Nemenyi from mlr (learners) \n")

obj = mlr::generateCritDifferencesData(bmr = bmk, measure = auc, p.value = 0.05, test = "nemenyi")
g2  = mlr::plotCritDifferences(obj = obj)

ggsave(g2, file = "../plots/cd_nemenyi.pdf", width = 6.95, height = 2.67)

# --------------------------------------------------------------------------------------------------
#  customized boxplots
# --------------------------------------------------------------------------------------------------

cat("- Customized boxplots\n")

perfs = getBMRPerformances(bmr = bmk, as.df = TRUE)
measures = c("auc", "bac", "f1")
colnames(perfs)[1:2] = c("Task", "Learner")

# Renaming task factors
perfs$Task = dplyr::recode_factor(perfs$Task,
  banned_champions = "Banned Champions",
  full = "Complete",
  picked_champions = "Picked Champions",
  picked_champions_players_statistics = "Picked Champions and\n Players Statistics",
  players_statistics = "Players Statistics")

perfs$Task = factor(perfs$Task, levels = c("Banned Champions", "Picked Champions",
  "Players Statistics", "Picked Champions and\n Players Statistics", "Complete"))

# Renaming learner factors
perfs$Learner = dplyr::recode_factor(perfs$Learner,
  RandomForest = "RF", Rpart = "DT", SVM = "SVM",
  LogReg = "LR", NaiveBayes = "NB", KKNN = "kNN")

# Reordeing learner factors
perfs$Learner = factor(perfs$Learner, levels = c("DT", "NB", "kNN",
  "SVM", "RF", "LR"))

# Plot AUC
sel = c("Task", "Learner", "iter", "auc")
sub = perfs[, sel]
g = ggplot(data = sub, mapping = aes(x = Learner, y = auc))
g = g + geom_boxplot() + facet_grid(.~Task) + theme_bw()
g = g + theme(axis.text.x = element_text(angle = 90, vjust = .5, hjust = 1))
ggsave(g, file = "../plots/customized_boxplot_auc.pdf", width = 8.17, height = 2.37)

# Plot BAC
sel = c("Task", "Learner", "iter", "bac")
sub = perfs[, sel]
g = ggplot(data = sub, mapping = aes(x = Learner, y = bac))
g = g + geom_boxplot() + facet_grid(.~Task) + theme_bw()
g = g + theme(axis.text.x = element_text(angle = 90, vjust = .5, hjust = 1))
ggsave(g, file = "../plots/customized_boxplot_bac.pdf", width = 8.17, height = 2.37)

# Plot BAC
sel = c("Task", "Learner", "iter", "f1")
sub = perfs[, sel]
g = ggplot(data = sub, mapping = aes(x = Learner, y = f1))
g = g + geom_boxplot() + facet_grid(.~Task) + theme_bw()
g = g + theme(axis.text.x = element_text(angle = 90, vjust = .5, hjust = 1))
ggsave(g, file = "../plots/customized_boxplot_f1.pdf", width = 8.17, height = 2.37)

# --------------------------------------------------------------------------------------------------
# PCA plot
# --------------------------------------------------------------------------------------------------

cat("- PCA plot for visualization \n")

dataset = read.csv("../data/dataset_players_statistics.csv")

Class = dataset$result
df = dataset[,-1]
df$result = NULL

objPCA = prcomp(df, scale = TRUE)
dfOut = as.data.frame(objPCA$x)
dfOut$Class = as.factor(Class)

p = ggplot(dfOut,aes(x=PC1,y=PC2,color=Class, shape=Class))
p = p + geom_point() + theme_bw()
p = p + scale_colour_manual(values = c("red", "black"))
ret = round(100 * summary(objPCA)$importance[2,], 2)
p = p + labs(x = paste0("PCA1 ", ret[1], "%"), y = paste0("PCA2 ", ret[2], "%"))
ggsave(p, file = "../plots/PCA_plot.pdf", width = 4.68, height = 3.61)

# PCA elbow curve
# sumRet = ret
# for(i in 1:length(ret)) {
  # sumRet[i] = sum(ret[1:i])
# }
# plot(x = 1:length(sumRet), y = sumRet)

# --------------------------------------------------------------------------------------------------
# Exporting data to Friedman-nemenyi
# Whe would like to compare different tasks (features)
# --------------------------------------------------------------------------------------------------

cat("- Export data to perform statistics\n")


dir.create("../stats/", showWarnings = FALSE)

# aggregated performances
df = getBMRPerformances(bmr = bmk, as.df = TRUE)
colnames(df)[1:2] = c("task", "learner")

for( i in c(4, 5, 6)) {

  data.sub = df[,c(1,2,3,i)]
  name = colnames(df)[i]
  print(name)

  tasks = unique(data.sub$task)
  lrns  = unique(data.sub$learner)

  aux.tasks = lapply(tasks, function(tsk) {
    aux.lrns = lapply(lrns, function(lrn) {
      sub = dplyr::filter(data.sub, task == tsk & learner == lrn)
      return(sub[4])
    })
    ret = do.call("rbind", aux.lrns)
    return(ret)
  })
  frd = do.call("cbind", aux.tasks)
  colnames(frd) = tasks
  write.csv(frd, file = paste0("../stats/friedman_", name, ".csv"))
}

# https://github.com/gabrieljaguiar/nemenyi
# Python command
# python3 nemenyi.py examples/friedman_bac.csv examples/friedman_bac.tex --h --ignore_first_column

cat("- Finished :)\n")

# --------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------
