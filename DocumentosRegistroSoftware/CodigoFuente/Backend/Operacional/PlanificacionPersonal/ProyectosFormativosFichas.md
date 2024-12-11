```
//ENTITY PROYECTOSFORMATIVOSFICHAS
package com.persona.Backend.Entity.Operational.PlanificacionFormativa;

import com.persona.Backend.Entity.BaseEntity;
import com.persona.Backend.Entity.Operational.GestionHorario.Ficha;

import jakarta.persistence.Entity;
import jakarta.persistence.FetchType;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.Table;

@Entity
@Table(name = "proyectos_formativos_fichas")
public class ProyectosFormativosFichas extends BaseEntity {

	@ManyToOne(fetch = FetchType.EAGER, optional = false)
	@JoinColumn(name = "proyecto_formativo_id", nullable = false, unique = false)
	private ProyectoFormativo proyectoFormativoId;

	@ManyToOne(fetch = FetchType.EAGER, optional = false)
	@JoinColumn(name = "ficha_id", nullable = false, unique = false)
	private Ficha fichaId;

	public ProyectoFormativo getProyectoFormativoId() {
		return proyectoFormativoId;
	}

	public void setProyectoFormativoId(ProyectoFormativo proyectoFormativoId) {
		this.proyectoFormativoId = proyectoFormativoId;
	}

	public Ficha getFichaId() {
		return fichaId;
	}

	public void setFichaId(Ficha fichaId) {
		this.fichaId = fichaId;
	}

}



//IREPOSITORY PROYECTOSFORMATIVOSFICHAS
package com.persona.Backend.IRepository.Operational.PlanificacionFormativa;

import org.springframework.stereotype.Repository;

import com.persona.Backend.Entity.Operational.PlanificacionFormativa.ProyectosFormativosFichas;
import com.persona.Backend.IRepository.IBaseRepository;

@Repository
public interface IProyectosFormativosFichasRepository extends IBaseRepository<ProyectosFormativosFichas, Long> {

}


//ISERVICE PROYECTOSFORMATIVOSFICHAS
package com.persona.Backend.IService.Operational.PlanificacionFormativa;

import com.persona.Backend.Entity.Operational.PlanificacionFormativa.ProyectosFormativosFichas;
import com.persona.Backend.IService.IBaseService;

public interface IProyectosFormativosFichasService extends IBaseService<ProyectosFormativosFichas>{

}

//SERVICE PROYECTOSFORMATIVOSFICHAS
package com.persona.Backend.Service.Operational.PlanificacionFormativa;

import org.springframework.stereotype.Service;

import com.persona.Backend.Entity.Operational.PlanificacionFormativa.ProyectosFormativosFichas;
import com.persona.Backend.IService.Operational.PlanificacionFormativa.IProyectosFormativosFichasService;
import com.persona.Backend.Service.BaseService;

@Service
public class ProyectosFormativosFichasService extends BaseService<ProyectosFormativosFichas> implements IProyectosFormativosFichasService {

}

//CONTROLLER PROYECTOSFORMATIVOSFICHAS
package com.persona.Backend.Controller.Operational.PlanificacionFormativa;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.persona.Backend.Controller.BaseController;
import com.persona.Backend.Entity.Operational.PlanificacionFormativa.ProyectosFormativosFichas;

@CrossOrigin("*")
@RestController
@RequestMapping("/api/v1/base/operational/planificacion_formativa/proyectos_formativos_fichas")
public class ProyectosFormativosFichasController extends BaseController<ProyectosFormativosFichas> {

}


```