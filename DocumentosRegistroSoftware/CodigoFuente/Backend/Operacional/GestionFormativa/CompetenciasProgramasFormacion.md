```
//ENTITY COMPETENCIASPROGRAMASFORMACION
package com.persona.Backend.Entity.Operational.GestionFormativa;

import com.persona.Backend.Entity.BaseEntity;

import jakarta.persistence.Entity;
import jakarta.persistence.FetchType;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.Table;

@Entity
@Table(name = "competencias_programas_formacion")
public class CompetenciasProgramasFormacion extends BaseEntity {

	@ManyToOne(fetch = FetchType.EAGER, optional = false)
	@JoinColumn(name = "programa_formacion_id", nullable = false, unique =false)
	private ProgramaFormacion programaFormacionId;

	@ManyToOne(fetch = FetchType.EAGER, optional = false)
	@JoinColumn(name = "competencia_id", nullable = false, unique = false)
	private Competencia competenciaId;

	public ProgramaFormacion getProgramaFormacionId() {
		return programaFormacionId;
	}

	public void setProgramaFormacionId(ProgramaFormacion programaFormacionId) {
		this.programaFormacionId = programaFormacionId;
	}

	public Competencia getCompetenciaId() {
		return competenciaId;
	}

	public void setCompetenciaId(Competencia competenciaId) {
		this.competenciaId = competenciaId;
	}
}
//IREPOSITORY COMPETENCIASPROGRAMASFORMACION
package com.persona.Backend.IRepository.Operational.GestionFormativa;

import org.springframework.stereotype.Repository;

import com.persona.Backend.Entity.Operational.GestionFormativa.CompetenciasProgramasFormacion;
import com.persona.Backend.IRepository.IBaseRepository;

@Repository
public interface ICompetenciasProgramasFormacionRepository extends IBaseRepository<CompetenciasProgramasFormacion, Long>{

}


//ISERVICE COMPETENCIASPROGRAMASFORMACION
package com.persona.Backend.IService.Operational.GestionFormativa;

import com.persona.Backend.Entity.Operational.GestionFormativa.CompetenciasProgramasFormacion;
import com.persona.Backend.IService.IBaseService;

public interface ICompetenciasProgramasFormacionService extends IBaseService<CompetenciasProgramasFormacion> {

}

//SERVICE COMPETENCIASPROGRAMASFORMACION
package com.persona.Backend.Service.Operational.GestionFormativa;

import org.springframework.stereotype.Service;

import com.persona.Backend.Entity.Operational.GestionFormativa.CompetenciasProgramasFormacion;
import com.persona.Backend.IService.Operational.GestionFormativa.ICompetenciasProgramasFormacionService;
import com.persona.Backend.Service.BaseService;

@Service
public class CompetenciasProgramasFormacionService extends BaseService<CompetenciasProgramasFormacion> implements ICompetenciasProgramasFormacionService{

}

//CONTROLLER COMPETENCIASPROGRAMASFORMACION
package com.persona.Backend.Controller.Operational.GestionFormativa;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.persona.Backend.Controller.BaseController;
import com.persona.Backend.Entity.Operational.GestionFormativa.CompetenciasProgramasFormacion;

@CrossOrigin("*")
@RestController
@RequestMapping("/api/v1/base/operational/gestion_formativa/competencias_programas_formacion")
public class CompetenciasProgramasFormacionController extends BaseController<CompetenciasProgramasFormacion>{

}

```