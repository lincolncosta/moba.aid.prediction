# --------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------
# install if you do not have the packages in your R system

# uncomment the following line to install packages
# install.packages(c("ggplot2", "partykit"))

library(mlr)
library(ggplot2)

# --------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------

dir.create("../plots/")

# loading data
load(file = "./benchmarking_results.RData") #bmk

# --------------------------------------------------------------------------------------------------
# boxplots
# --------------------------------------------------------------------------------------------------

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

  rf.models = mlr::getBMRModels(bmr=bmk, learner.ids = "classif.randomForest",
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
# --------------------------------------------------------------------------------------------------
