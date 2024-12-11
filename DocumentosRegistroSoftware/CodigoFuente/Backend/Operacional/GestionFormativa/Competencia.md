```
//ENTITY COMPETENCIA
package com.persona.Backend.IRepository.Operational.GestionFormativa;

import org.springframework.stereotype.Repository;

import com.persona.Backend.Entity.Operational.GestionFormativa.Competencia;
import com.persona.Backend.IRepository.IBaseRepository;

@Repository
public interface ICompetenciaRepository extends IBaseRepository<Competencia, Long>{

}
//IREPOSITORY COMPETENCIA
package com.persona.Backend.IRepository.Operational.GestionFormativa;

import org.springframework.stereotype.Repository;

import com.persona.Backend.Entity.Operational.GestionFormativa.Competencia;
import com.persona.Backend.IRepository.IBaseRepository;

@Repository
public interface ICompetenciaRepository extends IBaseRepository<Competencia, Long>{

}
//ISERVICE COMPETENCIA
package com.persona.Backend.IService.Operational.GestionFormativa;

import com.persona.Backend.Entity.Operational.GestionFormativa.Competencia;
import com.persona.Backend.IService.IBaseService;

public interface ICompetenciaService extends IBaseService<Competencia>{

}
//SERVICE COMPETENCIA
package com.persona.Backend.Service.Operational.GestionFormativa;

import org.springframework.stereotype.Service;

import com.persona.Backend.Entity.Operational.GestionFormativa.Competencia;
import com.persona.Backend.IService.Operational.GestionFormativa.ICompetenciaService;
import com.persona.Backend.Service.BaseService;

@Service
public class CompetenciaService extends BaseService<Competencia> implements ICompetenciaService {

}
//CONTROLLER COMPETENCIA
package com.persona.Backend.Controller.Operational.GestionFormativa;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.persona.Backend.Controller.BaseController;
import com.persona.Backend.Entity.Operational.GestionFormativa.Competencia;

@CrossOrigin("*")
@RestController
@RequestMapping("/api/v1/base/operational/gestion_formativa/competencia")
public class CompetenciaController extends BaseController<Competencia>{

}



```
