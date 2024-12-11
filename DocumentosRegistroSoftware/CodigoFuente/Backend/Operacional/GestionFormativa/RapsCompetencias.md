```
//ENTITY RAPSCOMPETENCIAS
package com.persona.Backend.Entity.Operational.GestionFormativa;

import com.persona.Backend.Entity.BaseEntity;

import jakarta.persistence.Entity;
import jakarta.persistence.FetchType;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.Table;

@Entity
@Table(name = "raps_competencias")
public class RapsCompetencias extends BaseEntity {

	@ManyToOne(fetch = FetchType.EAGER, optional = false)
	@JoinColumn(name = "rap_id", nullable = false, unique = false)
	private Rap rapId;

	@ManyToOne(fetch = FetchType.EAGER, optional = false)
	@JoinColumn(name = "competencia_id", nullable = false, unique = false)
	private Competencia competenciaId;

	public Rap getRapId() {
		return rapId;
	}

	public void setRapId(Rap rapId) {
		this.rapId = rapId;
	}

	public Competencia getCompetenciaId() {
		return competenciaId;
	}

	public void setCompetenciaId(Competencia competenciaId) {
		this.competenciaId = competenciaId;
	}
	
	
}
//IREPOSITORY RAPSCOMPETENCIAS
package com.persona.Backend.IRepository.Operational.GestionFormativa;

import org.springframework.stereotype.Repository;

import com.persona.Backend.Entity.Operational.GestionFormativa.RapsCompetencias;
import com.persona.Backend.IRepository.IBaseRepository;


@Repository
public interface IRapsCompetenciasRepository extends IBaseRepository<RapsCompetencias, Long>{

}
//ISERVICE RAPSCOMPETENCIAS
package com.persona.Backend.IService.Operational.GestionFormativa;

import com.persona.Backend.Entity.Operational.GestionFormativa.RapsCompetencias;
import com.persona.Backend.IService.IBaseService;

public interface IRapsCompetenciasService extends IBaseService<RapsCompetencias>{

}
//SERVICE RAPSCOMPETENCIAS
package com.persona.Backend.Service.Operational.GestionFormativa;

import org.springframework.stereotype.Service;

import com.persona.Backend.Entity.Operational.GestionFormativa.RapsCompetencias;
import com.persona.Backend.IService.Operational.GestionFormativa.IRapsCompetenciasService;
import com.persona.Backend.Service.BaseService;

@Service
public class RapsCompetenciasService extends BaseService<RapsCompetencias> implements IRapsCompetenciasService{

}
//CONTROLLER RAPSCOMPETENCIAS
package com.persona.Backend.Controller.Operational.GestionFormativa;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.persona.Backend.Controller.BaseController;
import com.persona.Backend.Entity.Operational.GestionFormativa.RapsCompetencias;

@CrossOrigin("*")
@RestController
@RequestMapping("/api/v1/base/operational/gestion_formativa/raps_competencias")
public class RapsCompetenciasController extends BaseController<RapsCompetencias>{

}


```