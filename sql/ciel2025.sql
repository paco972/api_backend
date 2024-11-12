CREATE DATABASE `ciel2025` ;
USE `ciel2025`;

--
-- Structure de la table `etudiant`
--
CREATE TABLE `etudiant` (
  `idetudiant` int(11) NOT NULL,
  `nom` varchar(45) NOT NULL,
  `prenom` varchar(45) NOT NULL,
  `email` varchar(45) DEFAULT NULL,
  `telephone` varchar(45) DEFAULT NULL
) ;

--
-- Index pour la table `etudiant`
--
ALTER TABLE `etudiant`
  ADD PRIMARY KEY (`idetudiant`);

--
-- AUTO_INCREMENT pour la table `etudiant`
--
ALTER TABLE `etudiant`
  MODIFY `idetudiant` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

--
-- Données de la table `etudiant`
--
INSERT INTO `etudiant` (`idetudiant`, `nom`, `prenom`, `email`, `telephone`) VALUES
(1, 'TERIEUR', 'Alex', 'alex.terieur@gmail.com', '+596696123456),
(2, 'TERIEUR', 'Alain', 'alain.terieur@gmail.com', '+596696654321');
